# Code Example:
# Let's consider a scenario where we have a media player application that supports different types of media files, 
# such as audio files (MP3, WAV) and video files (MP4, AVI).

# Without applying the ISP, we might have a single interface like this:


class MediaPlayer:
    
    def play_audio(self, audio_file):
        raise NotImplementedError
    
    def play_video(self, video_file):
        raise NotImplementedError
    
    def stop_audio(self):
        raise NotImplementedError
    
    def stop_video(self):
        raise NotImplementedError
    
    def adjust_audio_volume(self, volume):
        raise NotImplementedError
    
    def adjust_video_brightness(self, brightness):
        raise NotImplementedError


# In this case, any class that implements the MediaPlayer interface would be forced to implement all the methods, even if it doesn't need them.

# For example, an audio player would have to implement the play_video, stop_video, and adjust_video_brightness methods, even though they are not relevant for audio playback.


# To adhere to the ISP, we can segregate the interface into smaller, more focused interfaces:

class AudioPlayer:
    def play_audio(self, audio_file):
        raise NotImplementedError
    
    def stop_audio(self):
        raise NotImplementedError
    
    def adjust_audio_volume(self, volume):
        raise NotImplementedError
    

class VideoPlayer:
    def play_video(self, video_file):
        raise NotImplementedError

    def stop_video(self):
        raise NotImplementedError
    
    def adjust_video_brightness(self, brightness):
        raise NotImplementedError
    
    

# Now, we can have separate implementations for audio and video players:

class MP3Player(AudioPlayer):
    def play_audio(self, audio_file):
        pass
    
    def stop_audio(self):
        pass
    
    def adjust_audio_volume(self, volume):
        pass
    
    
class AviVideoPlayer(VideoPlayer):
    def play_video(self, video_file):
        pass

    def stop_video(self):
        pass
    
    def adjust_video_brightness(self, brightness):
        pass
    

# By segregating the interfaces, each class only needs to implement the methods it actually requires. 
# This not only makes the code more maintainable but also prevents clients from being forced to depend on methods they don't use.

# If we need a class that supports both audio and video playback, we can create a new class that implements both interfaces:

class MultimediaPlayer(AudioPlayer, VideoPlayer):
    pass'




# Violating the Interface Segregation Principle
# Let's consider an example where a Worker interface is designed to handle different types of workers 
# (e.g., programmers, robots) in a factory setting. The Worker interface has methods that are not applicable to all types of workers.

# Code That Violates ISP


from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class HumanWorker(Worker):
    def work(self):
        print("Human working...")

    def eat(self):
        print("Human eating...")

class RobotWorker(Worker):
    def work(self):
        print("Robot working...")

    def eat(self):
        raise NotImplementedError("Robots don't need to eat!")
    


# Problems with the Above Example
# Unnecessary Methods: The RobotWorker class is forced to implement the eat() method, even though it doesn't make sense for a robot to have this capability. 
#                     This violates ISP because the RobotWorker is dependent on an interface that includes methods it does not use.
# Fragile Design: This design can lead to issues when maintaining or extending the system. For example, adding a new method to the Worker 
#                 interface would require all implementing classes to update, even if the method isn't relevant to them.



# Refactoring to Adhere to ISP
# To adhere to the Interface Segregation Principle, we can split the Worker interface into smaller, more specific interfaces that cater to different types of workers.

# Code That Adheres to ISP


from abc import ABC, abstractmethod

# Separate interfaces
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

# Implementing classes
class HumanWorker(Workable, Eatable):
    def work(self):
        print("Human working...")

    def eat(self):
        print("Human eating...")

class RobotWorker(Workable):
    def work(self):
        print("Robot working...")
