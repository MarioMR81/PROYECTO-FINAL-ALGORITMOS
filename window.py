# Aqui tenemos nuestra librerias a utilizar en nuestro programa 
from tkinter import *
import codecs
from tkinter import messagebox

class User:
  
  # Aqui estan definidos nuestros datos que se mostraran dentro del programa
  def __init__(self):
    self.name = 'Mario Rene Quiñonez Quinteros' 
    self.carnet = 7690212086 

class Window:
    # Atributos de mi ventana
    def __init__(self, alerts):
        self.user = User()
        self.title = "Gestión de archivos"
        self.size = "850x800"
        self.resizable = False
        self.PATH_UPDATE = ''
        self.alerts = alerts

        
    
    # La configuracion principal de la ventana  como por ejemplo titulo, tamaño y el texto que se recibe
    def init_window(self):
        window = Tk()
        self.window = window
        
        window.title(self.title)

        window.geometry(self.size)

        if self.resizable:
            window.resizable(1, 1)
        else:
            window.resizable(0, 0)
    
        self.path = StringVar()
        self.PATH_UPDATE = self.path
        self.content_file = StringVar()
        self.data_box = Frame(self.window, width=1000)

    # Aqui se muestra el metodo para agregar texto a la ventana o interfaz grafica. Como parametro recibe el texto, el row y el column para ubicarlo en la ventana
    def add_text(self, txt, row, column, header):
        text = Label(self.window, text=txt)
        text.grid(row=row, column=column, columnspan=3)

        #Aqui estan las especificaciones de la ventana tamaño, color, tipo de letra ubicacion y tamaño
        if header:
            text.config(
                fg="white",
                bg="#003850",
                font=("Open Sans", 24),
                padx=250,
                pady=10
            )

    # Aqui se arma el formulario atraves de los inputs y labels de las entradas
    def form_for_files(self):
        # Este label es para la ruta del archivo Muy Importante
        label_path = Label(self.window, text="Ruta del archivo: " )
        label_path.grid(row=2, column=0, sticky=W)

        input_path = Entry(self.window, width=50, textvariable=self.path)
        input_path.grid(row=3, column=0, pady=20, padx=5, sticky=W)

        # Este Botón para abrir el archivo selecionado con la ruta
        button_open_file = Button(self.window, text="Abrir", command=self.read_file)
        button_open_file.grid(row=3, column=1)
        button_open_file.config(padx=10, pady=8)

        # Este label es para mostrar el contenido del archivo
        label_content = Label(self.window, text="El contenido del archivo es: ")
        label_content.grid(row=4, column=0, sticky=W)

        self.input_content = Text(self.window)
        self.input_content.grid(row=5, column=0, pady=20, sticky=W)

        buttons_box = Frame(self.window)
        buttons_box.grid(row=9, column=0, columnspan=3)

        buttons_box.propagate(False)

        # Este Botón nos mostrara los datos del usuario o nuestros datos
        button_data = Button(buttons_box, text="Datos", command=self.show_data)
        button_data.grid(row=1, column=0, sticky=S)
        button_data.config(padx=10, pady=8, width=10)

        # Este Botón es muy importante nos guardara la informacion que ingresemos en el textbox
        button_save = Button(buttons_box, text="Guardar", command=self.update_file)
        button_save.grid(row=1, column=1, sticky=S)
        button_save.config(padx=10, pady=8)

        # Este Botón realiza la funcion para salir del programa
        button_close = Button(buttons_box, text="Salir", command=quit)
        button_close.grid(row=1, column=2, sticky=S)
        button_close.config(padx=10, pady=8)

    # Es el metodo para leer el archivo
    def read_file(self):

        self.PATH_UPDATE = self.path.get()

        try:
            # Estamos solicitando permiso para abrir el archivo como lectura
            read_file = codecs.open(self.path.get(), "r", 'utf-8')
            
            content_file = read_file.read()

            # Aqui estamos indicando que borre el contendio del texto y agrege el nuevo contenido
            self.input_content.delete('1.0', END)
            self.input_content.insert('1.0', content_file)

            # Estamos indicando o mostrando el pop-pop que nos indica que el archivo se abrio correctamente
            self.alerts.showinfo(
                title="Abrir archivo",
                message='El Archivo se abrio correctamente'
            )
            
            read_file.close()

            # Metodo para mostrar el mensaje de error y si se ingresa mal la ruta del archivo
        except Exception as error:
            type_error = type(error).__name__

            self.alerts.showerror(
                title="Abrir archivo",
                message=f'{type_error}: Verificar la ruta del archivo Porfavor'
            )
    
    # Funcion principal para actualizar el archivo que solicitamos desde la ruta de acceso solicitamos permisos para editar dicho archivo y actualizar
    def update_file(self):
        try:
            
            file_to_update = codecs.open(self.PATH_UPDATE, "w", 'utf-8')

            file_to_update.write(self.input_content.get('1.0', END))

            # Funcion Para mostrar mensaje que el archivo se actualizo correctamente 
            self.alerts.showinfo(
                title="Actualizar archivo",
                message='Archivo Guardado correctamente'
            )

            file_to_update.close()

            self.input_content.delete('1.0', END)
            self.path.set('')
        
        except Exception as error:

            type_error = type(error).__name__

            # Funcion para mostrar un mensaje que el archivo no se pudo guardar correctamente
            self.alerts.showerror(
                title="Actualizar archivo",
                message=f'{type_error}: ERROR al guardar archivo'
            )

        # Funcion con varios Labels que ayudaran para mostrar los datos del usuario del programa
    def show_data(self):
        self.data_box.config(
            padx=20,
            pady=20,
            bg="#00546c"
        )
        self.data_box.grid(row=1, columnspan=3)

        label_name = Label(self.data_box, text=f'Nombre: { self.user.name }')
        label_name.grid(row=1, column=0)
        label_name.config(bg='#00546c')

        label_carnet = Label(self.data_box, text=f'Carné: { self.user.carnet }')
        label_carnet.grid(row=2, column=0)
        label_carnet.config(bg='#00546c')

        separator = Label(self.data_box, text=' ')
        separator.grid(row=3, column=0)
        separator.config(bg='#00546c')

        button_close_data = Button(self.data_box, text='Cerrar Datos', command=self.hide_data)
        button_close_data.grid(row=4, columnspan=2)

    # Funcion para ocultar la ventana o pop-pop que muestra los datos del usuario como el nombre y numero de carné
    def hide_data(self):
        self.data_box.grid_remove()

    def load_window(self):
        self.window.mainloop()
    
program = Window(messagebox)
program.init_window()

program.add_text('Gestión de archivos', 0, 0, True)

# Funcion para mostrar el formulario del programa o parte grafica
program.form_for_files()

# Llamado para cargar la ventana principal
program.load_window() 