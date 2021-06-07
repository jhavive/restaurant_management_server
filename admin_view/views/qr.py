import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
from rest_framework.decorators import api_view
from django.views.static import serve
import os
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
# from scipy.misc import imread
import os
import numpy as np
import glob
import imageio

@api_view(['GET',])
def get_qr(request):
    filepath = os.path.join(
        settings.BASE_DIR,
        'public',
        'qr',
        request.GET.get('hotel'),
        request.GET.get('file')+'.jpeg'
    )
    print(filepath)
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

def plotImage(f):
    print(f)
    im = imageio.imread(f)
    plt.imshow(im)
    a = plt.gca()
    a.get_xaxis().set_visible(False)  # We don't need axis ticks
    a.get_yaxis().set_visible(False)


@api_view(['GET',])
def get_qr_pdf(request):
    if not request.GET.get('hotel') or request.GET.get('hotel') == "undefined":
        return Response({
            "message": "Incorrect Information"
        }, status=400)

    pdf_file_path = os.path.join(
        settings.BASE_DIR,
        'public',
        'qr',
        request.GET.get('hotel') + '.pdf'
    )
    if os.path.isfile(pdf_file_path):
        pdf_file_path = os.path.join(pdf_file_path)
        return serve(request, os.path.basename(pdf_file_path), os.path.dirname(pdf_file_path))

    files = glob.glob(os.path.join(
        settings.BASE_DIR,
        'public',
        'qr',
        request.GET.get('hotel'),
        '*.jpeg'
    ))


    pp = PdfPages(pdf_file_path)
    for file in files:
        plt.subplot(121)
        plotImage(file)
        pp.savefig(plt.gcf())

    pp.close()
    return serve(request, os.path.basename(pdf_file_path), os.path.dirname(pdf_file_path))