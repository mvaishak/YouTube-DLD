from pytube import YouTube 


print('''
                                                                                                                                            
                                                                                                                                           
                                                                                
                                     .,,,..                                     
                            ,,,,,,,,,,,,,,,,,,,,,,,.                            
                       ,,,,,,                     .,,,,,                        
                    ,,,,.                             .,,,,                     
                  ,,,.                                    ,,,.                  
                ,,,                                         ,,,.                
              ,,,                                             ,,,               
             ,,,                                               ,,,.             
            ,,,                                                 .,,.            
           ,,,                                                   ,,,            
          .,,                                                     ,,,,,,,,,     
     .,,,,,,,                                                            .,,,.  
   ,,,.                                                                     ,,, 
 ,,,                                                                         ,,,
 ,,                                    ,,,                                   .,,
,,,                                    ,,,                                   .,,
 ,,,                                   ,,,                                  .,,.
  ,,,                                  ,,,                                 ,,,  
    ,,,,.                              ,,,                             .,,,,    
       .,,,,,,,,,,,,,,,,,,             ,,,             ,,,,,,,,,,,,,,,,,.       
                              .,,,     ,,,     ,,,                              
                                .,,,.  ,,,  ,,,,                                
                                   ,,,,,,,,,,,                                  
                                     .,,,,,         
                                       ,,


                                Y O U T U B E - DLD                                               
                                                                                                                                                                                                                             
''')

link = input("Enter a link ...\n   ")
try:
    video = YouTube(str(link))
except:
    print(".......Um we've got a problem")
    print('.......Check if the entered link is valid and try again')
    exit('.......Exiting app!')
res = input('Pick a number for the resolution you want!\n   0: 360\n   1: 720\n   2: 1080\n')
options = ['360p', '720p', '1080p']
chosen_stream = video.streams.filter(file_extension = 'mp4', resolution = options[int(res)])
if len(chosen_stream)<1:
  print(".....Looks like we don't have anything that resolution :( ")
  exit('.......Exiting app!')
print('Downloading {}'.format(video.title))
download_stream = chosen_stream[0].download('/home/vaishak/Downloads')