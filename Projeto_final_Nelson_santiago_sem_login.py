import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import hashlib
import sqlite3
import mysql.connector





# Connect to database
connexion = mysql.connector.connect(host='localhost', user='root', password='yQh1iAe17@')
cursor = connexion.cursor()

# Create database (if not exists)
cursor.execute("CREATE DATABASE IF NOT EXISTS music_interface")
connexion.commit()

# Using database
cursor.execute("USE music_interface")

# Creating table soundtracks
cursor.execute("""CREATE TABLE IF NOT EXISTS soundtracks (
                    soundtrack_id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(100),
                    duration TIME,
                    genre VARCHAR(50),
                    artist_id INT,
                    album_id INT,
                    FOREIGN KEY (artist_id) REFERENCES artists(artist_id),
                    FOREIGN KEY (album_id) REFERENCES albums(album_id)
                )""")
connexion.commit()

# Creating table albums
cursor.execute("""CREATE TABLE IF NOT EXISTS albums (
                    album_id INT AUTO_INCREMENT PRIMARY KEY,
                    album_name VARCHAR(100)
                )""")
connexion.commit()

# Creating table artists
cursor.execute("""CREATE TABLE IF NOT EXISTS artists (
                    artist_id INT AUTO_INCREMENT PRIMARY KEY,
                    artist_name VARCHAR(50)
                )""")
connexion.commit()


def connect_database():
    return mysql.connector.connect(host='localhost', user='root', password='yQh1iAe17@', database='music_interface')

# Function to insert a soundtrack into database
def insert_soundtrack():
    title = entry_title.get().strip()
    duration = entry_duration.get().strip()
    genre = entry_genre.get().strip()
    artist_id = artist_combobox.get().split(' - ')[0]  # Get the artist ID from the selected value
    album_id = album_combobox.get().split(' - ')[0]  # Get the album ID from the selected value

    print(f"Title: '{title}'")
    print(f"Duration: '{duration}'")
    print(f"Genre: '{genre}'")
    print(f"Artist ID: '{artist_id}'")
    print(f"Album ID: '{album_id}'")

    # Verifica se algum campo está vazio
    if not (title and duration and genre and artist_id and album_id):
        messagebox.showerror("Error", "Please fulfill all fields.")
        return

    try:
        cursor.execute(
            "INSERT INTO soundtracks (title, duration, genre, artist_id, album_id) VALUES (%s, %s, %s, %s, %s)",
            (title, duration, genre, artist_id, album_id))

        connexion.commit()
        last_id = cursor.lastrowid
        print("Soundtrack inserted successfully.")
        messagebox.showinfo("Success!", f"Soundtrack {last_id} inserted successfully.")
        entry_title.delete(0, tk.END)
        entry_duration.delete(0, tk.END)
        entry_genre.delete(0, tk.END)
    except Exception as e:
        print(f"Error inserting soundtrack: {e}")
        messagebox.showerror("Error!", "Error while inserting soundtrack.")

# Function to fetch existing artists from the database and populate the combobox
def fetch_existing_artists():
    try:
        cursor.execute("SELECT artist_id, artist_name FROM artists")
        artists_list = cursor.fetchall()
        sorted_artist_ids = sorted([f"{artist[0]} - {artist[1]}" for artist in artists_list], key=lambda x: int(x.split(' - ')[0]))
        return sorted_artist_ids
    except Exception as e:
        messagebox.showerror("Error", f"Error while fetching artists: {e}")

def fetch_existing_albums():
    try:
        cursor.execute("SELECT album_id, album_name FROM albums")
        albums_list = cursor.fetchall()
        sorted_album_ids = sorted([f"{album[0]} - {album[1]}" for album in albums_list],
                                  key=lambda x: int(x.split(' - ')[0]))
        return sorted_album_ids
    except Exception as e:
        messagebox.showerror("Error", f"Error while fetching albums: {e}")
#TODO
# Function to fetch existing soundtrack IDs from the database
def fetch_existing_soundtrack_ids():
    try:
        cursor.execute("SELECT soundtracks_id FROM soundtracks")
        soundtrack_ids = [str(soundtrack[0]) for soundtrack in cursor.fetchall()]
        sorted_soundtrack_ids = sorted(soundtrack_ids, key=int)
        return sorted_soundtrack_ids
    except Exception as e:
        messagebox.showerror("Error", f"Error while fetching soundtrack IDs: {e}")
# Function to insert an artist into database

def insert_artist():
    artist_name = entry_artist_name.get().strip()
    if artist_name:
        try:
            cursor.execute(
                "INSERT INTO artists (artist_name) VALUES (%s)",
                (artist_name,))

            connexion.commit()
            messagebox.showinfo("Success!", "Artist inserted successfully.")
            entry_album_name.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error!", f"Error while inserting artist: {e}")
    else:
        messagebox.showerror("Error", "Please fulfill all fields.")

# Function to insert an album into database
def insert_album():
    album_name = entry_album_name.get().strip()
    if album_name:
        try:
            cursor.execute(
                "INSERT INTO albums (album_name) VALUES (%s)",
                (album_name,))

            connexion.commit()
            messagebox.showinfo("Success!", "Album inserted successfully.")
            entry_album_name.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error!", f"Error while inserting album: {e}")
    else:
        messagebox.showerror("Error", "Please fulfill all fields.")

# Function to edit a soundtrack into database
def edit_soundtrack():
    print("Edit Soundtrack button clicked")
    soundtracks_id = combo_soundtracks_id.get()
    title = entry_title_edit.get().strip()
    duration = entry_duration_edit.get().strip()
    genre = entry_genre_edit.get().strip()
    artist_id = combo_edit_artist_id.get().split(' - ')[0]
    album_id = combo_edit_album_id.get().split(' - ')[0]

    if soundtracks_id and title and duration and genre and artist_id and album_id:
        try:
            connexion = connect_database()
            cursor = connexion.cursor()
            cursor.execute("UPDATE soundtracks SET title = %s, duration = %s, genre = %s, "
                           "artist_id = %s, album_id = %s WHERE soundtracks_id = %s",
                           (title, duration, genre, artist_id, album_id, soundtracks_id))

            connexion.commit()
            messagebox.showinfo("Success!", "Soundtrack was successfully edited.")
            combo_soundtracks_id.delete(0, tk.END)
            entry_title_edit.delete(0, tk.END)
            entry_duration_edit.delete(0, tk.END)
            entry_genre_edit.delete(0, tk.END)
            combo_edit_artist_id.delete(0, tk.END)
            combo_edit_album_id.delete(0, tk.END)
            cursor.close()
            connexion.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error while editing soundtrack: {e}")
    else:
        messagebox.showerror("Error", "Please fulfill all fields.")
def edit_album():
    album_id = entry_album_id.get()
    album_name = entry_album_name_edit.get().strip()
    if album_id and album_name:
        try:
            connexion = connect_database()
            cursor = connexion.cursor()
            cursor.execute("UPDATE albums SET album_name = %s WHERE album_id = %s",
                           (album_name, album_id))
            connexion.commit()
            messagebox.showinfo("Success!", "Album was successfully edited.")
            entry_album_id.delete(0, tk.END)
            entry_album_name_edit.delete(0, tk.END)
            cursor.close()
            connexion.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error while editing album: {e}")
    else:
        messagebox.showerror("Error", "Please fulfill all fields.")
# Function to remove a soundtrack from database
def remove_soundtrack():
    soundtracks_id = entry_remove_soundtracks_id.get()
    if soundtracks_id:
        try:
            cursor.execute("DELETE FROM soundtracks WHERE soundtracks_id = %s", (soundtracks_id,))
            connexion.commit()
            messagebox.showinfo("Success!", "Soundtrack successfully removed.")
            entry_remove_soundtracks_id.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Error while removing soundtrack: {e}")
    else:
        messagebox.showerror("Error", "Please insert the soundtrack ID.")

# Function to remove an album from database
"""def remove_album():
    album_id = entry_remove_album_id.get()
    if album_id:
        try:
            cursor.execute("DELETE FROM albums WHERE album_id = %s", (album_id,))
            connexion.commit()
            messagebox.showinfo("Success!", "Album successfully removed.")
            entry_remove_album_id.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Error while removing album: {e}")
    else:
        messagebox.showerror("Error", "Please insert the album ID.")"""

# Function to list all soundtracks from database
def list_soundtracks():
    try:
        cursor.execute("SELECT * FROM soundtracks")
        soundtracks_list = cursor.fetchall()

        # Clear the current content from the TextBox
        text_box_soundtracks.delete(1.0, tk.END)

        # Insert the headers
        text_box_soundtracks.insert(tk.END, "ID\tTitle\tDuration\tGenre\tArtist ID\tAlbum ID\n")

        # Insert each song to show up
        for soundtrack in soundtracks_list:
            text_box_soundtracks.insert(tk.END,
                                        f"{soundtrack[0]}\t{soundtrack[1]}\t{soundtrack[2]}\t{soundtrack[3]}\t{soundtrack[4]}\t{soundtrack[5]}\n")
    except Exception as e:
        messagebox.showerror("Error", f"Error while listing soundtracks: {e}")

# Function to list all albums from database
def list_albums():
    try:
        cursor.execute("SELECT * FROM albums")
        albums_list = cursor.fetchall()

        # Clear the current TextBox content
        text_box_albums.delete(1.0, tk.END)

        # Insert the headers
        text_box_albums.insert(tk.END, "Album ID\tAlbum Name\n")

        # Insert each album from database to show up
        for album in albums_list:
            text_box_albums.insert(tk.END, f"{album[0]}\t{album[1]}\n")
    except Exception as e:
        messagebox.showerror("Error", f"Error while listing albums: {e}")

# Function to list all artists from database
def list_artists():
    try:
        cursor.execute("SELECT * FROM artists")
        artists_list = cursor.fetchall()

        # clear the current text box content from database
        text_box_artists.delete(1.0, tk.END)

        # Insert the headers
        text_box_artists.insert(tk.END, "Artist ID\tArtist Name\n")

        # Inserts each artist from database to show up
        for artist in artists_list:
            text_box_artists.insert(tk.END, f"{artist[0]}\t{artist[1]}\n")
    except Exception as e:
        messagebox.showerror("Error", f"Error while listing artists: {e}")

# Function to save the database to a text file
def save_database():
    try:
        #It recovers the name from the current database
        database_name = "music_interface"

        #It creates the name of txt file based on database name
        filename = f"{database_name}.txt"

        # Opens the file to write on it
        with open(filename, "w") as file:
            # It writes the data from soundtracks table
            file.write("Tabela: soundtracks\n")
            file.write("{:^15} {:^30} {:^10} {:^20} {:^15} {:^15}\n".format(
                "soundtrack_id", "title", "duration", "genre", "artist_id", "album_id"))
            cursor.execute("SELECT * FROM soundtracks")
            soundtracks_list = cursor.fetchall()
            for soundtrack in soundtracks_list:
                file.write("{:^15} {:^30} {:^10} {:^20} {:^15} {:^15}\n".format(*map(str, soundtrack)))

            # It writes the data from albums table
            file.write("\nTabela: albums\n")
            file.write("{:^10} {:^50}\n".format("album_id", "album_name"))
            cursor.execute("SELECT * FROM albums")
            albums_list = cursor.fetchall()
            for album in albums_list:
                file.write("{:^10} {:^50}\n".format(*map(str, album)))

            #It writes the data from artists table
            file.write("\nTabela: artists\n")
            file.write("{:^10} {:^50}\n".format("artist_id", "artist_name"))
            cursor.execute("SELECT * FROM artists")
            artists_list = cursor.fetchall()
            for artist in artists_list:
                file.write("{:^10} {:^50}\n".format(*map(str, artist)))

        #It shows a successfull message
        messagebox.showinfo("Sucesso", f"Dados salvos em {filename} com sucesso.")
    except Exception as e:
        #It shows an error message if something is wrong
        messagebox.showerror("Erro", f"Erro ao salvar os dados: {e}")

# Function to exit the application
def exit_application():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Music Interface Nelson Santiago's App")
root.iconbitmap("musicalnote1_83800.ico")

# Style the application with ttkthemes
style = ttk.Style()
style.theme_use('clam')  # You can choose other themes like 'arc', 'clearlooks', etc.

# Set up a notebook to organize different sections of the interface
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Frame for Soundtracks section
frame_soundtracks = ttk.Frame(notebook)
notebook.add(frame_soundtracks, text='Soundtracks')

# Frame for Artists section
frame_artists = ttk.Frame(notebook)
notebook.add(frame_artists, text='Artists')

# Entry widget and label for listing artists
label_list_artists = ttk.Label(frame_artists, text="List of Artists:")
label_list_artists.grid(row=3, column=0, padx=5, pady=5)
text_box_artists = tk.Text(frame_artists, height=10, width=50)
text_box_artists.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
button_list_artists = ttk.Button(frame_artists, text="List Artists", command=list_artists)
button_list_artists.grid(row=5, column=0, padx=5, pady=5)

# Entry widgets and labels for adding albums
label_artist_name = ttk.Label(frame_artists, text="Artist Name:")
label_artist_name.grid(row=1, column=0, padx=5, pady=5)
entry_artist_name = ttk.Entry(frame_artists)
entry_artist_name.grid(row=1, column=1, padx=5, pady=5)

button_insert_artist = ttk.Button(frame_artists, text="Insert Artist", command=insert_artist)
button_insert_artist.grid(row=2, columnspan=2, padx=5, pady=5)


# Add buttons to save the database and exit the application
button_save_database = ttk.Button(root, text="Save Database", command=save_database)
button_save_database.pack(side="left", padx=10, pady=10)
button_exit = ttk.Button(root, text="Exit", command=exit_application)
button_exit.pack(side="left", padx=10, pady=10)


# Entry widgets and labels for adding soundtracks
label_title = ttk.Label(frame_soundtracks, text="Title:")
label_title.grid(row=1, column=0, padx=5, pady=5)
entry_title = ttk.Entry(frame_soundtracks)
entry_title.grid(row=1, column=1, padx=5, pady=5)

label_duration = ttk.Label(frame_soundtracks, text="Duration:")
label_duration.grid(row=2, column=0, padx=5, pady=5)
entry_duration = ttk.Entry(frame_soundtracks)
entry_duration.grid(row=2, column=1, padx=5, pady=5)

label_genre = ttk.Label(frame_soundtracks, text="Genre:")
label_genre.grid(row=3, column=0, padx=5, pady=5)
entry_genre = ttk.Entry(frame_soundtracks)
entry_genre.grid(row=3, column=1, padx=5, pady=5)

# Combobox for selecting existing artists
label_artist_id = ttk.Label(frame_soundtracks, text="Artist:")
label_artist_id.grid(row=4, column=0, padx=5, pady=5)
artist_combobox = ttk.Combobox(frame_soundtracks, values=fetch_existing_artists())
artist_combobox.grid(row=4, column=1, padx=5, pady=5)

# Combobox for selecting existing albums
label_album_id = ttk.Label(frame_soundtracks, text="Album:")
label_album_id.grid(row=5, column=0, padx=5, pady=5)
album_combobox = ttk.Combobox(frame_soundtracks, values=fetch_existing_albums())
album_combobox.grid(row=5, column=1, padx=5, pady=5)

label_album_id = ttk.Label(frame_soundtracks, text="Album ID:")
label_album_id.grid(row=5, column=0, padx=5, pady=5)
#entry_album_id = ttk.Entry(frame_soundtracks)
#entry_album_id.grid(row=5, column=1, padx=5, pady=5)

button_insert_soundtrack = ttk.Button(frame_soundtracks, text="Insert Soundtrack", command=insert_soundtrack)
button_insert_soundtrack.grid(row=6, columnspan=2, padx=5, pady=5)

# Entry widget and label for listing soundtracks
label_list_soundtracks = ttk.Label(frame_soundtracks, text="List of Soundtracks:")
label_list_soundtracks.grid(row=7, column=0, padx=5, pady=5)
text_box_soundtracks = tk.Text(frame_soundtracks, height=10, width=50)
text_box_soundtracks.grid(row=8, column=0, columnspan=2, padx=5, pady=5)
button_list_soundtracks = ttk.Button(frame_soundtracks, text="List Soundtracks", command=list_soundtracks)
button_list_soundtracks.grid(row=9, column=0, padx=5, pady=5)

# Frame for Albums section
frame_albums = ttk.Frame(notebook)
notebook.add(frame_albums, text='Albums')

# Entry widgets and labels for adding albums
label_album_name = ttk.Label(frame_albums, text="Album Name:")
label_album_name.grid(row=1, column=0, padx=5, pady=5)
entry_album_name = ttk.Entry(frame_albums)
entry_album_name.grid(row=1, column=1, padx=5, pady=5)

button_insert_album = ttk.Button(frame_albums, text="Insert Album", command=insert_album)
button_insert_album.grid(row=2, columnspan=2, padx=5, pady=5)

# Entry widget and label for listing albums
label_list_albums = ttk.Label(frame_albums, text="List of Albums:")
label_list_albums.grid(row=3, column=0, padx=5, pady=5)
text_box_albums = tk.Text(frame_albums, height=10, width=50)
text_box_albums.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
button_list_albums = ttk.Button(frame_albums, text="List Albums", command=list_albums)
button_list_albums.grid(row=5, column=0, padx=5, pady=5)

# Frame for Editing section
frame_editing = ttk.Frame(notebook)
notebook.add(frame_editing, text='Editing')

# Entry widgets and labels for editing soundtracks
label_soundtracks_id = ttk.Label(frame_editing, text="Soundtrack ID:")
label_soundtracks_id.grid(row=1, column=0, padx=5, pady=5)

# Combobox for selecting existing soundtrack IDs
soundtrack_ids = fetch_existing_soundtrack_ids()
combo_soundtracks_id = ttk.Combobox(frame_editing, values=soundtrack_ids)
combo_soundtracks_id.grid(row=1, column=1, padx=5, pady=5)


label_edit_title = ttk.Label(frame_editing, text="Title:")
label_edit_title.grid(row=2, column=0, padx=5, pady=5)
entry_title_edit = ttk.Entry(frame_editing)
entry_title_edit.grid(row=2, column=1, padx=5, pady=5)

label_edit_duration = ttk.Label(frame_editing, text="Duration:")
label_edit_duration.grid(row=3, column=0, padx=5, pady=5)
entry_duration_edit = ttk.Entry(frame_editing)
entry_duration_edit.grid(row=3, column=1, padx=5, pady=5)

label_edit_genre = ttk.Label(frame_editing, text="Genre:")
label_edit_genre.grid(row=4, column=0, padx=5, pady=5)
entry_genre_edit = ttk.Entry(frame_editing)
entry_genre_edit.grid(row=4, column=1, padx=5, pady=5)

label_edit_artist_id = ttk.Label(frame_editing, text="Artist ID:")
label_edit_artist_id.grid(row=5, column=0, padx=5, pady=5)
combo_edit_artist_id = ttk.Combobox(frame_editing, values=fetch_existing_artists())
combo_edit_artist_id.grid(row=5, column=1, padx=5, pady=5)

label_edit_album_id = ttk.Label(frame_editing, text="Album ID:")
label_edit_album_id.grid(row=6, column=0, padx=5, pady=5)
combo_edit_album_id = ttk.Combobox(frame_editing, values=fetch_existing_albums())
combo_edit_album_id.grid(row=6, column=1, padx=5, pady=5)

button_edit_soundtrack = ttk.Button(frame_editing, text="Edit Soundtrack", command=edit_soundtrack)
button_edit_soundtrack.grid(row=7, columnspan=2, padx=5, pady=5)


# Entry widgets and labels for editing albums
label_album_id_edit = ttk.Label(frame_editing, text="Album ID:")
label_album_id_edit.grid(row=8, column=0, padx=5, pady=5)
entry_album_id = ttk.Entry(frame_editing)
entry_album_id.grid(row=8, column=1, padx=5, pady=5)

label_album_name_edit = ttk.Label(frame_editing, text="Album Name:")
label_album_name_edit.grid(row=9, column=0, padx=5, pady=5)
entry_album_name_edit = ttk.Entry(frame_editing)
entry_album_name_edit.grid(row=9, column=1, padx=5, pady=5)

button_edit_album = ttk.Button(frame_editing, text="Edit Album", command=edit_album)
button_edit_album.grid(row=10, columnspan=2, padx=5, pady=5)

# Frame for Removing section
frame_removing = ttk.Frame(notebook)
notebook.add(frame_removing, text='Removing')

# Entry widgets and labels for removing soundtracks
label_remove_soundtracks_id = ttk.Label(frame_removing, text="Soundtrack ID:")
label_remove_soundtracks_id.grid(row=1, column=0, padx=5, pady=5)
entry_remove_soundtracks_id = ttk.Entry(frame_removing)
entry_remove_soundtracks_id.grid(row=1, column=1, padx=5, pady=5)

button_remove_soundtrack = ttk.Button(frame_removing, text="Remove Soundtrack", command=remove_soundtrack)
button_remove_soundtrack.grid(row=2, columnspan=2, padx=5, pady=5)

# Entry widgets and labels for removing albums
#label_remove_album_id = ttk.Label(frame_removing, text="Album ID:")
#label_remove_album_id.grid(row=3, column=0, padx=5, pady=5)
#entry_remove_album_id = ttk.Entry(frame_removing)
#entry_remove_album_id.grid(row=3, column=1, padx=5, pady=5)

#button_remove_album = ttk.Button(frame_removing, text="Remove Album", command=remove_album)
#button_remove_album.grid(row=4, columnspan=2, padx=5, pady=5)

root.mainloop()
