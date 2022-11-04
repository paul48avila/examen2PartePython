#convertidor de csv a pdf

import csv


def csv_to_pdf():
    #abrir el archivo csv
    with open('ventas.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        #creamos el archivo pdf
        with open('ventas.pdf', 'w') as pdf_file:
            #recorremos el archivo csv
            for line in csv_reader:
                #escribimos en el archivo pdf
                pdf_file.write(line)


if __name__ == '__main__':
    csv_to_pdf()
    
                

