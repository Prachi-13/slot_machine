from django.shortcuts import render, redirect

from .models import GameSession
from .utils import generate_random_string, generate_random_blocks
from core.enums.symbols import Symbols
from django.contrib.auth.decorators import login_required

# Create your views here.


def slot_machine(request):
    session_id = request.session.get("session_id")
    try:
        game_session = GameSession.objects.get(pk=session_id)
    except GameSession.DoesNotExist:
        requested_user = request.user
        if requested_user.is_authenticated:
            game_session = GameSession(player_name=requested_user.username, is_guest=False, user=requested_user)
            # transfer those credits to game session
            if requested_user.userprofile.credits >= 10:
                requested_user.userprofile.credits -= 10
                game_session.credits = 10
            else:
                game_session.credits = requested_user.userprofile.credits
                requested_user.userprofile.credits = 0
            requested_user.userprofile.save()
        else:
            random_str = generate_random_string()
            game_session = GameSession(player_name=f"Guest{random_str}")
        game_session.save()
        request.session['session_id'] = game_session.id
    context = {"game_session": game_session}
    return render(request, 'slot_machine.html', context)

def game_over(request):
    return render(request, 'game_over.html')

def pull_lever(request):
    session_id = request.session.get("session_id")
    if session_id:
        game_session = GameSession.objects.get(pk=session_id)
    else:
        return redirect("slot_machine")

    if game_session.credits > 0:
        result = generate_random_blocks(game_session.credits)
        reward = 0
        if all(symbol == result[0] for symbol in result):
            if result[0] == Symbols.cherry.name:
                reward = 10
            elif result[0] == Symbols.lemon.name:
                reward = 20
            elif result[0] == Symbols.orange.name:
                reward = 30
            elif result[0] == Symbols.watermelon.name:
                reward = 40

        game_session.credits -= 1
        game_session.game_state = ", ".join(result)
        game_session.credits += reward
        game_session.save()

    return redirect("slot_machine")


@login_required
def cash_out(request):
    session_id = request.session.get("session_id")
    if session_id:
        game_session = GameSession.objects.get(pk=session_id)
        user_profile = request.user.userprofile
        user_profile.credits += game_session.credits
        user_profile.save()

        game_session.delete()
        del request.session['session_id']
    return redirect("dashboard")
