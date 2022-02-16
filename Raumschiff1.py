import pygame # füge die Bibliothek ein / add the library 
import time # füge die Zeit ein / insert the time
from cmath import cos, sin
from pygame import constants # importierung der Pygame Bibliothek
from pygame.constants import(QUIT,KEYDOWN,KEYUP,K_ESCAPE,K_TAB,K_KP_PLUS,K_KP_MINUS,K_F10,K_LEFT,K_RIGHT,K_UP,K_DOWN,K_SPACE,MOUSEBUTTONDOWN) # importierung der Knoepfe /import of buttons
import os # Importiert des kompletten os-Moduls  /  Import the complete os module
import random# Importiert eine zufälige Zahl /  Imports a single number


class Settings:
    screen_width = 800
    screen_height = 500 
    inner_rect = pygame.Rect(
    100, 100, screen_width - 200, screen_height - 200)
    fps = 60 # Bilder pro sekunde /  Frames per second
    pygame.display.set_caption("Das Rauschiff-Game")
    file_path = os.path.dirname(os.path.abspath(__file__)) # Datei Pfad /   File Path
    image_path = os.path.join(file_path,"images") # Was für eine Art Dateityp wird importiert /  What kind of file type is imported
    def get_dim(): # Dimme den Bildschirm /  Dim the screen
        return (Settings.screen_width, Settings.screen_height)# Die Rueckgabe der Bildschirmgroeße  /The returns the screen size

        
        
class Background(pygame.sprite.Sprite): #Hauptklasse  Hintergrund /Main Class Background
    def __init__(self, filename):# Definiere die Funktion / Define the function 
        super().__init__() # Erbe die Klasse  Background / Inherit the Background class
        self.image = pygame.image.load(os.path.join(Settings.image_path, filename)).convert() # Ladet das PNG.Image in die Klasse Hintergrund rein /# Load the PNG. Image in the Background class 
        self.rect = pygame.transform.scale(self.image,Settings.get_dim()) # Dimme das PNG.IMAGE /  Dim the  PNG.IMAGE file
        self.rect = self.image.get_rect() # Gibt Informationen über die Position und Groeße des Rechtecks zurueck / returns information about the position and size of the rectangle

    def draw(self,screen): # Zeichnet das Foto im Bildschirm ein / Enter the photo on the screen
        screen.blit(self.image,self.rect)  # Gibt Informationen ueber die Position und Groesse des Images zurueck /  Returns information about the position and size of the image.


class Raumschiff(pygame.sprite.Sprite): #  Hauptklasse Jet / Main Class Jet
    def __init__(self, filename):  # Definiert die Funktion  (self,filename) / Define the function (self,filename)
        self.image = pygame.image.load(os.path.join(Settings.image_path, filename)).convert_alpha() # Ladet das PNG.Image in die Klasse Hintergrund rein /# Load the PNG. Image in the Background class  
        self.rect = self.image.get_rect() # Gibt Informationen ueber die Position und Größe des Rechtecks zurueck / returns information about the position and size of the rectangle
        self.rect.top  = 450  # Die Position der Hoehe / The position of the height
        self.rect.left = 400 # Die Position Links / The position Links
        self.time_jump = 3000 # Wann wieder gesprungen werden kann / When  do you can jump 
        self.speed_v =  0 # Geschwindigkeit Vertikal / Speed Vertical
        self.speed_h =  0 # Geschwindigkeit Horisontal / Speed Horizontal
        self.speed = 5 # Geschwindigkeit / Speed 
        self.radius = 15 # Legt den Radius fest / Sets the radius
        self.direction_h = 0 # Richtung Horisontal /  Direction Horisontal
        self.direction_v =  0  # Richtung Vertikal /  Direction Vertical
        self.coordinates  
                                                                                         # randompos wird aufgerufen

    def coordinates(self):
        self.rect.left = random.randint(0, Settings.screen_width - self.rect.width)    

    def draw(self,screen): # Zeichnet das Foto im Bildschirm ein / Enter the photo on the screen
         screen.blit(self.image,self.rect)  # Gibt Informationen über die Position und Groeße des Images zurueck /  Returns information about the position and size of the image
       
    def update(self): #  aktualisiere / Update 
      self.rect = self.rect.move(self.speed_h,self.speed_v) # Bewege dich in der Geschwindigkeit Horizontal und mit Vertikalen Geschwindigkeit /Move horizontally and vertically at speed
      if self.rect.bottom > Settings.screen_height: # Wenn der Boden Groeßer als die Einstellungen von der Bildschirmhoehe ist /If the floor is larger than settings from the screen hight
            self.rect.bottom = Settings.screen_height  # Wenn  der Boden Gleich so gross ist wie die  Einstellungen von der BildschirmHoehe  / When the floor is equal to the settings of the screen hight
      if self.rect.right> Settings.screen_width: # Wenn die Rechte Seite Groeßer als Einstellungen von der Bildschirmbreite ist /If right is larger than settings from the screen width
            self.rect.right = Settings.screen_width # Wenn die Rechte Seite  Gleich so gross ist wie  die Einstellungen von der Bildschirmbreite /If the right side is equal to the settings of the screen width
      if self.rect.left < 0: # Wenn die Seite links kleiner als Null ist/  If the page on the left is less than zero
          self.rect.left = 0 # Wenn die Seite links gleich groß mit Null ist/   If the page on the left is the same size as zero
      if self.rect.top < 0: # Wenn die Seite oben kleiner als Null ist/  If the page on the top is less than zero
          self.rect.top = 0 # Wenn die Seite gleich groß mit Null ist/  If the page is the same size as zero
   
   
  
    def move_stop(self): # Nach dem Bewegen komme zum stehen / After moving, come to a standstill
        self.speed_h = self.speed_v = 0 # Berechnungs Koordina    ten/  Calculation coordinates
    
    def move_left(self):  # Bewege dich nach links /  Move to the left
        self.image =   pygame.transform.rotate(self.image,22.5)


    def angle(self,angle):
        self.speed_x = self.speed_x - sin(angle)
        self.speed_y = self.speed_y - cos(angle)
      
    
    
    def move_right(self): # Bewege dich nach rechts /  Move to the right
       self.image =   pygame.transform.rotate(self.image,22.5)
      

    
    def move_up(self,angle):  # Bewege dich  zurück /  Move to the back
        self.speed_x = self.speed_x - sin(angle)
        self.speed_y = self.speed_y - cos(angle)


    def move_up(self):    # Bewege dich nach vorn /  Move to the front
        self.speed_v = -1 * self.speed  # Berechnungs Koordinaten/  Calculation coordinates
    
    def move_down(self):  # Bewege dich  zurück /  Move to the back
        self.speed_v = 1 * self.speed  # Berechnungs Koordinaten/  Calculation coordinates






class Asteroid(pygame.sprite.Sprite): #  Hauptklasse Alien / Main Class Alien
    def __init__(self): # Definiere die Funktion  mit  (self) / Define the function with  (self)
        super().__init__() # Definiere die Funktion  (self) / Define the function (self,filename)
        a = random.randint(1, 3) # Es wird ein Image.PNG Augewaelt was  am Ende mit einer Zahl 0 bis .. Endet / It get  an image.PNG it ends with the number 0 until ...
        self.image = self.image = pygame.image.load(os.path.join(Settings.image_path,f"asteroid{a}.png")).convert_alpha() # Lade das PNG.Image in die Klasse Alien rein /# Load the PNG. Image in the Alien  class 
        self.rect = self.image.get_rect()  # Gibt Informationen über die Position und Groesse des Rechtecks zurueck / returns information about the position and size of the rectangle
        self.rect.top = 0 # Die Position der Hoehe / The position of the height
        self.randomposition() # Greift auf die Funktion randomposition zu / Accesses the randomposition function
        self.speed = random.randint(1,4) # Die Geschwindigkeit der Aliens wariert zwischen 1 bis 4
  
    def randomposition(self): # Die Position des Aliens / The position of the Alien
        self.rect.left  = random.randint(0, Settings.screen_width) #Die Kordinaten der Position  / The return of time and storage from the Enter function

    def update(self):  #  aktualisiere / Update 
        self.rect.move_ip(0,self.speed) # bewege den Alien in platz = move the alien into place
        if self.rect.top > Settings.screen_height: # Die höhe ist groesser als d  ieBildschirm hoehe /The height is greater than the screen height
            self.kill() # Der Alien soll verschwinden / The alien should disappear 
    
            
    def draw(self, screen): #Zeichne das Alien im Game /Zeichne das Alien im Game
       screen.blit(self.image, self.rect) # Gibt Informationen ueber die Position und Groesse des Images zurueck /  Returns information about the position and size of the image.


class Game(object): #Hauptklasse Game / Main Class Game
    def __init__(self):# Definiere die Funktion  mit  (self) / Define the function with  (self)
        pygame.init() # pygame wird initalisiert /pygame is initalized
        self.screen = pygame.display.set_mode(Settings.get_dim()) #Dimme den Bildschirm /  Dim the  Display
        self.clock = pygame.time.Clock() # Es wird  die Zeit im spiel eingefuegt = The time is inserted into the game
        self.background = Background("2021_11_17_Sternen_Himmel.png") # Ladet das Foto in der Klasse Hintergrund rein /Loads the photo in the Background class
        self.raumschiff = Raumschiff("2022_02_08_Raumschiff.png") # Ladet das Foto in der Klasse Jet rein /Loads the photo in the Jet class
        self.all_asteroids = pygame.sprite.Group() # Alle Aliens werden in einer sprite.Grupe hergestellt zum dublizieren = All aliens are in a sprite. Group made for duplication
        pygame.sprite.spritecollide(self.raumschiff,self.all_asteroids, True) # Die Variable Prueft auf Kollision / The variable Checks for collision
        self.time_between_asteroidbirth = 2000 # Es sponnen jede 2Sekunden Aliens / Aliens spun every 2 seconds
        self.time_next_possible_asteroidbirth = pygame.time.get_ticks() #Die moegliche Alien Zeit wird berechnet / Die possible alien time is calculated
        self.between_break = 1000 #Die Zeit der unterbrechnung /The time of the interrupt
        self.live = 1
        self.time_between_break = pygame.time.get_ticks() #Die moegliche unterbrechnung  wird berechnet /The possible sub-calculation will be calculated
      #  self.font_sitze = pygame.font.Font(pygame.font.get_default_font(),20) #Es wird die Score groesse eingestellt und  angezeigt /The score size is set and displayed
        self.font_bigsitze = pygame.font.Font(pygame.font.get_default_font(),50)#Es wird die Game Over  groesse eingestellt und  angezeigt /The Game Over size is set and displayed

       

    
          
    def watch_for_events(self):
        for event in pygame.event.get():                               
            if event.type == QUIT:                                  
                 self.running = False                                 # Fenster wird zum schließen aufgefordert
            elif event.type == KEYDOWN:                              #                         gedrükt
                if event.key == K_ESCAPE:                            # Wenn die Escape Taste            wurde
                    self.running = False                             # setzt self.running auf False. Damit wird es weiter unten zum schließen aufgefordert
                elif event.key == K_LEFT:                            # Bei Tastendruck von Pfeiltaste links
                    self.raumschiff.move_left()                          # Käfer läuft nach links
                elif event.key == K_RIGHT:                           # Bei Tastendruck von Pfeiltaste rechts
                    self.raumschiff.move_right()                         # Käfer läuft nach rechts  
                elif event.key == K_UP:                              # Bei Tastendruck von Pfeiltaste oben
                    self.raumschiff.move_up()                            # Käfer läuft nach oben
                elif event.key == K_DOWN:                            # Bei Tastendruck von Pfeiltaste unten
                    self.raumschiff.move_down()                          # Käfer läuft nach unten                                                   
                elif event.type == KEYUP: 
                     self.raumschiff.move_stop()                                # Beim loslassen der Pfeiltasten
                if event.key == K_LEFT or event.key == K_RIGHT or event.key == K_UP or event.key == K_DOWN: 
                  

         

                    self.raumschiff.update()
                    pygame.display.flip()
  

                      
           
    def draw(self): # Die Funktion Zeichne / The Draw function
        self.background.draw(self.screen) # Zeichne den Hintergrund Fenster / Draw the background on the windows
        self.all_asteroids.draw(self.screen) # Zeichne die Aliens in Fenster / Draw the Aliens on the windows
        self.raumschiff.draw(self.screen) # Zeichne die Jets in Fenster / Draw the jet on the windows
        pygame.display.flip() # Aktualisiert nur einen bestimmten Bereich / Updates only a specific area
        
    def update(self):   #  aktualisiere / Update 
        self.dection_time_between_asteroid() # Die Zeit zwischen den Aliens/ The time between the aliens
        if pygame.time.get_ticks() > self.time_next_possible_asteroidbirth: # Die Berechnung der Zeit wann Aliens spornen sollen / Calculating the time when aliens should spur
           a = Asteroid() # Eine Variable fuer Alien /A variable for alien
           option = 10 # Das Festlegen  der Optionen / the settings of the Setting 
           while option > 0: # Die der Optionen sollen kleiner als null sein /The options should be less than zero
             if pygame.sprite.spritecollide(a, self.all_asteroids, False): # Die Kolision der Aliens mit den Jet /The collision of the aliens with the jet
                 a.randomposition() # Mit einer Variable und Fubktion wird  die Position ermittelt /The position is determined with a variable and function
                 option -= 1 #  Die option  wird auf minus 1 gesetzt /The option is set to minus 1
             else: # oder / else 
               self.all_asteroids.add(Asteroid()) # Fuege alle Aliens ein /Join all aliens
               break # Unterbreche die Funktion / break the function
           self.time_next_possible_asteroidbirth = pygame.time.get_ticks() + self.time_between_asteroidbirth # Legt die Zeit fest wann ein euer Alien gespornt erden soll / Set the time when the Alien is sporn
        self.raumschiff.update() # Aktualisiere Jet / Update Jet
        self.all_asteroids.update() # Aktualisiere Aliens / Update Aktualisiere Aliens
        if pygame.sprite.spritecollide(self.raumschiff,self.all_asteroids, False): # Wenn der Jet mit den Aliens Kollidiert  /When the jet collides with the aliens
            self.live -=1 #  Ziehe ein Leben ab bei einer kollision mit einem Alien / Pull a live at a  collision with a Alien 
            self.raumschiff.coordinates() # Jet bekommt neue Koordinaten / Jet gets new coordinates 
            if self.live <=0: # Wenn das Leben kleiner als 0 ist / If the live is small as 0
               self.game_over()  # Man hat verloren / You have lose 


    def game_over(self): #funktion Game / function Game
        text = self.font_bigsitze.render("Game Over",True, (255,0,0)) # Zeigt am Ende des Spiels Game Over  in der Farbe rot an /
        rect = text.get_rect() # pygame wird initalisiert /pygame is initalized
        rect.centerx = Settings.screen_width //2 # Die Position fuer die breite  /  The position for the wight
        rect.centery = Settings.screen_height //2 - 50  # Die Position fuer die hoehe /  The position for the hight
        self.screen.blit(text, rect) # Es ist in Pygame rect ist eine eigene  Klasse um die Position des Texts fest zu legen /It is in Pygame rect his  own class to set the position of the text
        rect = text.get_rect() # text wird initalisiert /text  is initalized
        pygame.display.flip()  # aktualisiert die Anzeige  des Bildschirm / refreshes the display of the screen
        time.sleep(4)  # Pause / break
        self.running = False  # Das Programm schliesst sich /  The program closes
    
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(Settings.get_dim())
   #     self.jet = pygame.sprite.GroupSingle(Jet())


    def run(self): # funktion run /function run
        self.running = True # Programm startet sich /Program starts
        while self.running: # Bringt die funktion zum laufen / Makes the function work
        #    self.clock.tick(60)
            self.clock.tick(Settings.fps) # Ist die Variable Zeit fuer die Bilder in Sekunde /Is the variable time for the frames in seconds
            self.watch_for_events() # Bringt die Funktion watch_for_event zu funktion / Makes the function watch_for_event to function
            self.update() # Bringe die Funktion Update zum laufen / Get the update function up and running
            self.draw() # Bringe die Funktion Zeichnen zum laufen / Make the Drawing function work
         
    def dection_time_between_asteroid(self): #Hauptklasse  dection_time_between_alien / Main Class  dection_time_between_alien
        if pygame.time.get_ticks() >= self.time_between_break:   # berechnet die Zeit des Spornen der Aliens / calculates the time of spurs of the aliens
          if self.time_between_asteroidbirth >= 15: # Die Zeit zwischen den Aliens = The time between the Aliens 
             self.time_between_asteroidbirth -= 10 #  Die Zeit zwischen den Aliens = The time between the Aliens 
          self.time_between_break = pygame.time.get_ticks() + self.time_between_break #  Die Zeit zwischen den Aliens = The time between the Aliens 

if __name__ == '__main__': 
    os.environ['SDL_VIDEO_WINDOW_POS'] = "10, 30" # Fenster Position / Position window

    game = Game() # Greift auf die Funktion Game zu /Accesses the Game feature
    game.run() # Greift auf die Funktion run von Game  /Accesses the run function of Game
