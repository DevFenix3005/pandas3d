from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from direct.gui.OnscreenText import OnscreenText  # Untuk menampilkan teks pada layar

class ActorControlExample(ShowBase):
    def __init__(self):
        super().__init__()
        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)
        
        # Load the Actor with animations
        self.panda = Actor(
            "models/panda-model",  # Model file
            {"walk": "models/panda-walk4"}  # Animasi file
        )
        self.panda.reparentTo(self.render)
        self.panda.setScale(0.005)
        self.panda.setPos(0, 10, 0)

        # Initial Animation
        self.panda.loop("walk")  # Start walking animation in a loop
        
        # Key bindings for animation controls
        self.accept("1", self.play_animation)  # Play animation once
        self.accept("2", self.loop_animation)  # Loop animation
        self.accept("3", self.stop_animation)  # Stop animation
        self.accept("4", self.pause_animation)  # Pause animation
        self.accept("5", self.resume_animation)  # Resume animation
        self.accept("6", self.pose_animation)  # Set pose at a specific frame
        
        # Add instruction text
        self.add_instructions()
    
    def play_animation(self):
        """Play the animation once."""
        self.panda.play("walk")
        print("Playing animation once.")
    
    def loop_animation(self):
        """Loop the animation indefinitely."""
        self.panda.loop("walk")
        print("Looping animation.")
    
    def stop_animation(self):
        """Stop the animation."""
        self.panda.stop()
        print("Stopping animation.")
    
    def pause_animation(self):
        """Pause the animation."""
        self.panda.pose("walk", self.panda.getCurrentFrame("walk"))
        print("Pausing animation.")
    
    def resume_animation(self):
        """Resume the animation from the current frame."""
        self.panda.loop("walk")
        print("Resuming animation.")
    
    def pose_animation(self):
        """Set the Actor to a specific pose (frame)."""
        frame = 10  # Example frame number
        self.panda.pose("walk", frame)
        print(f"Setting pose at frame {frame}.")
    
    def add_instructions(self):
        """Display instructions on the screen using OnscreenText."""
        instructions = [
            "1: Play animation once",
            "2: Loop animation",
            "3: Stop animation",
            "4: Pause animation",
            "5: Resume animation",
            "6: Pose animation at frame 10",
        ]
        for i, text in enumerate(instructions):
            OnscreenText(
                text=text,
                pos=(-1.2, 0.9 - i * 0.1),  # Posisi teks di layar
                scale=0.05,  # Ukuran teks
                fg=(1, 1, 1, 1),  # Warna teks (putih)
                align=0,  # Perataan kiri
                mayChange=False  # Teks tidak akan diubah
            )

# Run the application
app = ActorControlExample()
app.run()