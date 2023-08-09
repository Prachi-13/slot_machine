from django.shortcuts import render, redirect
from game_session.models import GameSession

from .forms import UserRegistrationForm

# Create your views here.
def home_page(request):
    return render(request, 'account/home.html')


def guest_login(request):
    return redirect("slot_machine")


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(data=request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            session_id = request.session.get('session_id')
            if not session_id:
                # create new session if it doesn't exists
                new_game_session = GameSession(user=new_user, is_guest=False, player_name=new_user.username)
                new_game_session.save()
                request.session['session_id'] = new_game_session.pk

            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})
