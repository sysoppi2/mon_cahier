from django.shortcuts import redirect, get_object_or_404, render
from mini_url.models import MiniURL
from mini_url.forms import MiniURLForm


def liste_url(request):
    """ Affichage des redirections """
    minis = MiniURL.objects.order_by('-nb_acces')

    return render(request, 'mini_url/liste_url.html', locals())


def nouvelle_url(request):
    """ Ajout d'une redirection """
    if request.method == "POST":
        form = MiniURLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(liste)
    else:
        form = MiniURLForm()

    return render(request, 'mini_url/nouvelle_url.html', {'form': form})


def redirection(request, code):
    """ Redirection vers l'URL enregistrée """
    mini = get_object_or_404(MiniURL, code=code)
    mini.nb_acces += 1
    mini.save()

    return redirect(mini.url, permanent=True)
