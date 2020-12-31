from django.shortcuts import render
from django.http import HttpResponse

# internal libraries
from exodest.modules import generators


def control(request):
    user = "billmanh"  # No login features at this time.
    u = generators.load_universe(user)
    context = {}
    return render(request, "exodest/control.html", context)


def solarsystem(request):
    user = "billmanh"  # No login features at this time.
    u = generators.new_universe(user)
    # The root path is different when running tests.
    generators.save_universe(u, test_world_name, root_path="")
    u = generators.load_universe(test_world_name, root_path="")
    data = u.children[0].children[0].get_planet_data()
    context = {"system": data}
    return render(request, "exodest/solarsystem/solarsystem.html", context)

