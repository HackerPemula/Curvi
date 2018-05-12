import comtypes.client
import os, sys
from PIL import Image
from fpdf import FPDF
from django.http import HttpResponse

basepath = os.path.abspath(os.path.dirname(sys.argv[0])) + '\\pdfconverter\\curiculum_vitae\\'

def file2PDF(request):
    try:
        filename = request.filename

        deck = None
        pdfformatindex = None
        extension = os.path.splitext(filename)

        if(extension[1] == ".pptx"):
            filetype = comtypes.client.CreateObject("Powerpoint.Application")
            filetype.Visible = 0
            deck = filetype.Presentations.Open(basepath + filename)
            pdfformatindex = 32

            deck.SaveAs(os.path.join(basepath, "..\\result\\" + extension[0] + ".pdf"), pdfformatindex)
            deck.Close()
            filetype.Quit()

        elif(extension[1] == ".doc" or extension[1] == ".docx"):
            filetype = comtypes.client.CreateObject("Word.Application")
            filetype.Visible = 0
            deck = filetype.Documents.Open(basepath + filename)
            pdfformatindex = 17

            deck.SaveAs(os.path.join(basepath, "..\\result\\" + extension[0] + ".pdf"), pdfformatindex)
            deck.Close()
            filetype.Quit()

        elif(extension[1] == ".xls" or extension[1] == ".xlsx"):
            filetype = comtypes.client.CreateObject("Excel.Application")
            filetype.Visible = 0
            deck = filetype.Workbooks.Open(basepath + filename)
            pdfformatindex = 17
            
            deck.SaveAs(os.path.join(basepath, "..\\result\\" + extension[0] + ".pdf"), pdfformatindex)
            deck.Close()
            filetype.Quit()

        elif(extension[1] == ".png" or extension[1] == ".jpg" or extension[1] == ".jpeg"):
            image = basepath + filename
            im = Image.open(image)
            im.save(basepath + extension[0] + ".png")
            image = basepath + extension[0] + ".png"

            pdf = FPDF()
            pdf.add_page()
            pdf.image(image)
            pdf.output(extension[0] + ".pdf", "F")

            os.rename(extension[0] + ".pdf", "pdfconverter\\result\\" + extension[0] + ".pdf")

        else:
            return HttpResponse(status=404)

        return HttpResponse("Success")
    except:
        return HttpResponse(status=400)
