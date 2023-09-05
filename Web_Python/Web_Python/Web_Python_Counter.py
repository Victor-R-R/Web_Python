# Creando una Web con Reflex
import reflex as rx

# Creamos una clase para contar
class State(rx.State):
    # Creamos el contador con enteros partiendo desde 0
    count: int=0
    
    # Definimos contador creciente
    def increment(self):
        self.count +=1

    # Definimos el contador decreciente
    def decrement(self):
        self.count -= 1

# Indicamos como queremos la Web
def index():
    # Creamos un contenedor con hstack para meter componentes de manera vertical
    return rx.vstack(
        # Ahora creamos uno horizontal para añadir todo
        rx.hstack(
            # Dentro del Stack creamos el boton
            rx.button(
                # Boton decreciente
                "Decrement",
                color_scheme = "red",
                border_radius = "1em",
                on_click = State.decrement,
            ),
            # Creamos la cabecera
            rx.heading(State.count, font_size="2em"),
            # Creamos el segundo boton
            rx.button(
                # Boton creciente
                "Increment",
                color_scheme = "green",
                border_radius = "1em",
                on_click = State.increment,
            )
    
        )
    )

app = rx.App()
app.add_page(index)
app.compile()