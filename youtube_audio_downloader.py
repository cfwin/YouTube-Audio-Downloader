import os
import subprocess
from tkinter import Tk, Label, Text, Entry, Button, filedialog, messagebox

def download_youtube_audio_as_mp3(url, output_folder):
    """Use yt-dlp to download YouTube audio in the highest quality and convert it to MP3"""
    try:
        # Construct output file path and name template
        output_template = os.path.join(output_folder, "%(title)s.%(ext)s")
        
        # yt-dlp download options
        ydl_opts = [
            'yt-dlp',
            '-f', 'bestaudio',  # Select best audio
            '--extract-audio',   # Extract audio only
            '--audio-format', 'mp3',  # Convert to MP3 format
            '--audio-quality', '0',   # Highest audio quality
            '-o', output_template,  # Output filename
            url
        ]
        
        # Use subprocess to run yt-dlp command
        subprocess.run(ydl_opts, check=True)
        print(f"Audio successfully downloaded and converted to MP3: {url}")
    
    except Exception as e:
        print(f"Error downloading and converting audio: {e}")

def batch_download_and_convert(youtube_urls, folder_path):
    """Batch download YouTube videos and convert to highest quality MP3"""
    for url in youtube_urls:
        download_youtube_audio_as_mp3(url, folder_path)

def select_folder():
    """Open folder selection dialog"""
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_entry.delete(0, "end")
        folder_entry.insert(0, folder_selected)

def start_download_and_convert():
    """Process user input YouTube links and start downloading and converting"""
    folder_path = folder_entry.get()
    youtube_urls = url_text.get("1.0", "end").strip().split('\n')  # Get multi-line input and split by line
    
    if not folder_path:
        messagebox.showerror("Error", "Please select a folder")
        return
    
    if not youtube_urls:
        messagebox.showerror("Error", "Please enter valid YouTube video links")
        return
    
    youtube_urls = [url.strip() for url in youtube_urls if url.strip()]  # Remove empty lines and whitespace
    batch_download_and_convert(youtube_urls, folder_path)
    messagebox.showinfo("Complete", "All audio files have been successfully downloaded and converted to MP3")

# Create Tkinter GUI
root = Tk()
root.title("YouTube Audio Downloader and Converter")

# Create and place labels and multi-line text box
Label(root, text="YouTube Video Links (one per line):").grid(row=0, column=0, padx=10, pady=10)
url_text = Text(root, width=50, height=10)  # Create multi-line text box
url_text.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Save to Folder:").grid(row=1, column=0, padx=10, pady=10)
folder_entry = Entry(root, width=50)  # Single-line text box to show selected folder path
folder_entry.grid(row=1, column=1, padx=10, pady=10)

# Create "Select Folder" button
folder_button = Button(root, text="Select Folder", command=select_folder)
folder_button.grid(row=1, column=2, padx=10, pady=10)

# Create "Start" button
start_button = Button(root, text="Start Download and Convert", command=start_download_and_convert)
start_button.grid(row=2, column=1, padx=10, pady=10)

# Run Tkinter main loop
root.mainloop()
