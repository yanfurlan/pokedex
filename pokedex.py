import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import json

class Pokedex:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokédex")
        self.root.geometry("500x750")  # Aumenta o tamanho da janela

        self.load_data()
        self.current_index = -1  # Inicialmente fora dos limites válidos
        self.dark_mode = False

        self.light_colors = {
            'bg': '#F0F0F0',
            'fg': 'black',
            'btn_bg': '#D3D3D3',
            'btn_fg': 'black',
            'border': '#A0A0A0'
        }

        self.create_widgets()
        self.apply_theme()
        self.show_initial_image()

    def load_data(self):
        with open('pokemons.json', 'r') as f:
            self.pokemons = json.load(f)

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame = tk.Frame(self.canvas, bd=5, relief=tk.RIDGE)
        self.canvas.create_window((0, 0), window=self.frame, anchor=tk.NW)

        self.frame.bind("<Configure>", self.on_frame_configure)

        self.title_frame = tk.Frame(self.frame, bg=self.light_colors['bg'])
        self.title_frame.pack(pady=10)

        self.label = tk.Label(self.title_frame, text="Pokédex", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=5)

        self.subtitle = tk.Label(self.title_frame, text="Região de Kanto", font=("Helvetica", 12, "bold"))
        self.subtitle.pack(pady=5)

        self.search_frame = tk.Frame(self.frame, bg=self.light_colors['bg'])
        self.search_frame.pack(pady=5)

        self.search_criteria = tk.StringVar(value='Nome')
        self.criteria_menu = tk.OptionMenu(self.search_frame, self.search_criteria, 'Nome', 'Número', 'Tipo')
        self.criteria_menu.config(font=("Helvetica", 12))
        self.criteria_menu.pack(side=tk.LEFT, padx=5)

        self.search_label = tk.Label(self.search_frame, text="Buscar:", font=("Helvetica", 12))
        self.search_label.pack(side=tk.LEFT, padx=5)

        self.search_entry = tk.Entry(self.search_frame, font=("Helvetica", 12))
        self.search_entry.pack(side=tk.LEFT, padx=5)

        self.search_button = tk.Button(self.search_frame, text="Buscar", command=self.search_pokemon, font=("Helvetica", 12))
        self.search_button.pack(side=tk.LEFT, padx=5)

        self.result_label = tk.Label(self.frame, text="", font=("Helvetica", 12), justify=tk.LEFT)
        self.result_label.pack(pady=10)

        self.image_label = tk.Label(self.frame, bd=2, relief=tk.SOLID)  # Adiciona contorno na imagem
        self.image_label.pack(pady=10)

        self.nav_frame = tk.Frame(self.frame)
        self.nav_frame.pack(pady=10)

        self.prev_button = tk.Button(self.nav_frame, text="Anterior", command=self.prev_pokemon, font=("Helvetica", 12))
        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.next_button = tk.Button(self.nav_frame, text="Próximo", command=self.next_pokemon, font=("Helvetica", 12))
        self.next_button.pack(side=tk.RIGHT, padx=10)

    def on_frame_configure(self, event):
        # Atualize a região de rolagem do canvas
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def apply_theme(self):
        colors = self.light_colors

        self.root.configure(bg=colors['bg'])
        self.frame.configure(bg=colors['bg'], bd=2, relief=tk.RIDGE, highlightbackground=colors['border'], highlightcolor=colors['border'], highlightthickness=2)
        self.title_frame.configure(bg=colors['bg'])
        self.label.configure(bg=colors['bg'], fg=colors['fg'])
        self.subtitle.configure(bg=colors['bg'], fg=colors['fg'])
        self.search_frame.configure(bg=colors['bg'])
        self.search_label.configure(bg=colors['bg'], fg=colors['fg'])
        self.search_entry.configure(bg=colors['btn_bg'], fg=colors['btn_fg'])
        self.search_button.configure(bg=colors['btn_bg'], fg=colors['btn_fg'])
        self.prev_button.configure(bg=colors['btn_bg'], fg=colors['btn_fg'])
        self.next_button.configure(bg=colors['btn_bg'], fg=colors['btn_fg'])
        self.result_label.configure(bg=colors['bg'], fg=colors['fg'])
        self.image_label.configure(bg=colors['bg'])

    def show_initial_image(self):
        # Carregar e exibir a imagem da Pokébola
        try:
            pokeball_image = Image.open(r'C:\Users\yanga\Desktop\Estudo\Pokedex\assets\pokeball.png')
            pokeball_image = pokeball_image.resize((150, 150), Image.Resampling.LANCZOS)
            self.pokeball_photo = ImageTk.PhotoImage(pokeball_image)
            self.image_label.config(image=self.pokeball_photo)
        except Exception as e:
            print(f"Error loading initial Pokéball image: {e}")

    def search_pokemon(self):
        query = self.search_entry.get().lower()
        criterion = self.search_criteria.get()

        if criterion == 'Tipo':
            # Divida a consulta em palavras e verifique se todas estão presentes no tipo do Pokémon
            query_words = set(query.split())
            results = [pokemon for pokemon in self.pokemons 
                       if query_words.issubset(set(t.lower() for t in pokemon['type']))]
            if results:
                self.display_search_results(results)
            else:
                self.result_label.config(text="Nenhum Pokémon encontrado com esse tipo!")
                self.show_initial_image()  # Mostrar a imagem da Pokébola
        else:
            # Buscar por nome ou número
            for i, pokemon in enumerate(self.pokemons):
                if criterion == 'Nome' and pokemon['name'].lower() == query:
                    self.current_index = i
                    self.display_pokemon(pokemon)
                    return
                elif criterion == 'Número' and str(pokemon['id']) == query:
                    self.current_index = i
                    self.display_pokemon(pokemon)
                    return
            self.result_label.config(text="Pokémon não encontrado!")
            self.image_label.config(image='')

    def display_pokemon(self, pokemon):
        # Formatar o texto com largura fixa para alinhamento
        text = (
            f"Número:      {str(pokemon['id']).rjust(3)}\n"
            f"Nome:        {pokemon['name'].ljust(15)}\n"
            f"Tipo:        {', '.join(pokemon['type']).ljust(15)}\n"
            f"HP:          {str(pokemon['hp']).rjust(3)}\n"
            f"Ataque:      {str(pokemon['attack']).rjust(3)}\n"
            f"Defesa:      {str(pokemon['defense']).rjust(3)}\n"
            f"Velocidade:  {str(pokemon['speed']).rjust(3)}"
        )
        self.result_label.config(text=text)

        # Carregar e exibir a imagem do Pokémon
        try:
            image = Image.open(pokemon['image'])
            image = image.resize((150, 150), Image.Resampling.LANCZOS)  # Ajustar o tamanho da imagem
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
        except Exception as e:
            self.image_label.config(image='')
            print(f"Error loading image: {e}")

    def display_search_results(self, results):
        # Exibir os resultados da busca por tipo
        results_text = "Resultados:\n"
        for pokemon in results:
            results_text += f"Número: {pokemon['id']} - Nome: {pokemon['name']}\n"
        self.result_label.config(text=results_text)
        self.show_initial_image()  # Mostrar a imagem da Pokébola

    def next_pokemon(self):
        # Avançar para o próximo Pokémon
        if self.current_index == -1:  # Se o índice estiver fora dos limites
            self.current_index = 0
        else:
            if self.current_index == len(self.pokemons) - 1:
                # Voltar ao layout inicial se já estiver no último Pokémon
                self.current_index = -1
                self.show_initial_image()
                self.result_label.config(text="")
                return
            else:
                self.current_index = (self.current_index + 1) % len(self.pokemons)
        
        # Exibir o Pokémon atual
        pokemon = self.pokemons[self.current_index]
        self.display_pokemon(pokemon)

    def prev_pokemon(self):
        # Voltar para o Pokémon anterior
        if self.current_index == -1:  # Se o índice estiver fora dos limites
            self.current_index = len(self.pokemons) - 1
        else:
            if self.current_index == 0:
                # Voltar ao layout inicial se estiver no primeiro Pokémon
                self.current_index = -1
                self.show_initial_image()
                self.result_label.config(text="")
                return
            else:
                self.current_index = (self.current_index - 1) % len(self.pokemons)
        
        # Exibir o Pokémon atual
        pokemon = self.pokemons[self.current_index]
        self.display_pokemon(pokemon)

if __name__ == "__main__":
    root = tk.Tk()
    app = Pokedex(root)
    root.mainloop()
