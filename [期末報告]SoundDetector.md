# Learning Journey Process

1. **Basic GUI Design with Tkinter**  
   - Learned to create a graphical user interface using `tkinter`, including:  
     - Windows (`Tk`)  
     - Buttons (`Button`)  
     - Canvas for image display (`Canvas`)

2. **Image Handling**  
   - Using `PIL.Image` and `ImageTk.PhotoImage` to:  
     - Load images  
     - Resize them  
     - Display on the canvas

3. **Sound Detection with Librosa**  
   - Analyzed audio files with `librosa` by:  
     - Loading audio  
     - Applying FFT for spectrum analysis  
     - Detecting specific frequency ranges (e.g., siren sound)

4. **Animation Using Canvas**  
   - Implemented object movement by updating image positions in a loop to create animations (ambulance and car).

5. **Multithreading for Smooth UI**  
   - Applied `threading` to run animations and sound detection without freezing the main application.

6. **Pygame for Sound Playback**  
   - Used `pygame.mixer` to:  
     - Load sound files  
     - Play the siren sound in a loop during animations

7. **Integrating Visuals, Audio, and Interaction**  
   - Combined animations, sound detection, and user interaction into a realistic ambulance simulation.

8. **Enhancing User Experience**  
   - Added text prompts and smooth transitions to simulate real-life scenarios, such as cars giving way to an ambulance.
