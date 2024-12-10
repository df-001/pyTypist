import pygame

def settingsMenu():
    # initializing the constructor 
    pygame.init() 
    
    # opens up a window 
    screen = pygame.display.set_mode((1920,1030)) 
    
    # white color 
    white = (255,255,255) 
    bgcolour = (16,16,32)
    
    # light shade of the button 
    color_light = (32,32,63) 
    
    # dark shade of the button 
    color_dark = (8,8,16) 
    
    # stores the width of the 
    # screen into a variable 
    width = screen.get_width() 
    
    # stores the height of the 
    # screen into a variable 
    height = screen.get_height() 
    
    # defining a font 
    font = pygame.font.SysFont("Sans", 64)
    smallfont = pygame.font.SysFont('Sans',32) 
    
    # rendering a text written in 
    # this font 
    titleText = font.render('typingProject' , True , white) 
    text150 = smallfont.render('150' , True , white) 
    text100 = smallfont.render('100' , True , white)
    text50 = smallfont.render('50' , True , white)

    running = True

    while running: 
        for ev in pygame.event.get(): 
            
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                
            #Checks if the mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                #Checks which button clicked
                #Returns to main program when clicked
                if width/2-300 <= mouse[0] <= width/2+140 and height/2-150 <= mouse[1] <= height/2+54: 
                    running, wordCount = False, 50
                    width/2,height/2,140,40
            #Button 100 Check
                elif width/2-300 <= mouse[0] <= width/2-46 and height/2-75 <= mouse[1] <= height/2+54: 
                    running, wordCount = False, 100
            #Button 150 Check
                elif width/2-300 <= mouse[0] <= width/2-46 and height/2 <= mouse[1] <= height/2+54: 
                    running, wordCount = False, 150
                    
        screen.fill(bgcolour) 

        mouse = pygame.mouse.get_pos() 

        
        #Title
        pygame.draw.rect(screen, white, [width, height, 0, 0])
        screen.blit(titleText, (width/2-300,height-800))
        #50 Count button
        pygame.draw.rect(screen,color_light,[width/2-300,height/2-150,254,54]) 
        pygame.draw.rect(screen,color_dark,[width/2-298,height/2-148,250,50])
        screen.blit(text50, (width/2-190,height/2-140)) 
        #100 Count button
        pygame.draw.rect(screen,color_light,[width/2-300,height/2-75,254,54]) 
        pygame.draw.rect(screen,color_dark,[width/2-298,height/2-73,250,50])
        screen.blit(text100, (width/2-200,height/2-65)) 
        #150 Count button
        pygame.draw.rect(screen,color_light,[width/2-300,height/2,254,54]) 
        pygame.draw.rect(screen,color_dark,[width/2-298,height/2+2,250,50])
        screen.blit(text150, (width/2-200,height/2+8)) 
        # updates the frames of the game 
        pygame.display.update() 
    return wordCount