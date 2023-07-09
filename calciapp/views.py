from django.shortcuts import render
from calciapp.models import Bmi_Users

def calc(request):
        return  render(request, "index.html")

def calculations(request):
        na= request.GET["name"]
        ag= request.GET["age"]
        ht= float(request.GET["height"])
        wt= float(request.GET["weight"])
        ph= request.GET["num"]
        bmi = (wt*100*100)/(ht*ht)

        weights_list = ["OVERWEIGHT", "UNDERWEIGHT", "NORMAL", "OBESITY"]

        images=[
                "myapp/overweight.jpg",
                "myapp/under_weight.jpg",
                "myapp/normal_weight.jpg",
                "myapp/obese.jpg"
                ]

        suggestions = [
                        "!!Some more exercise and healthy food habits needed to fall into normal",
                        "oops!!Its urgent for you to consult your dietitian and time for some healthy food",
                        "Good !!keep going and follow healthy diet",
                        "oh dear!!Its Time for you to consult your dietitian and time for some healthy food..Delay in  this will cause lot more problems",
                     ]
        if bmi < 18.5:
                res=weights_list[1]
                im=images[1]
                su = suggestions[1]
        elif bmi >=18.5 and bmi <=24.9:
                res = weights_list[2]
                im = images[2]
                su = suggestions[2]

        elif bmi >= 25.0 and bmi <= 29.9:
                res = weights_list[0]
                im = images[0]
                su = suggestions[0]

        else:
                res = weights_list[3]
                im = images[3]
                su = suggestions[3]



        dict_store={"result":bmi, "cate":res, "img":im,"sug":su}

        Bmi_Users.objects.all()
        b=Bmi_Users(name=na, age=ag, height=ht, weight=wt, ph_no=ph, bmi_index=bmi, status=res)
        b.save()

        return render(request, 'calculation.html', dict_store)







