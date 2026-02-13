import json
def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def helper(videos):
    try:
        with open('youtube.txt','w') as file:    
         json.dump(videos,file)
    except FileExistsError:
        return[]
data= 'youtube.txt'
def delete_video(videos):
    list_of_videos(videos)
    delete = int(input("Enter the video no. to delete."))
    if(1<=delete<=len(videos)):
        del videos[delete-1]
        helper(videos)
    else:print("invalid index input")    

def search_video(videos):
    list_of_videos(videos)
    print("*"*180)
    search=int(input("Enter the video no. to search"))
    if(1<=search<=len(videos)):
        for i,point in enumerate(videos,start=1):
            if(i==search):
                return i
            break
       
        print(f"{i}.{point['name']}\nDuration:{point['time']}\nLink:{point['link']}")
    
    else:
        print("Invalid input")        

    
def Update_video(videos):
    list_of_videos(videos)
    index = int(input("Enter a video no. to update.:"))
    if(1<=index<=len(videos)):
        name = input("Enter the new video name.:")
        time = input("Enter the new video time.:")
        link = input("Enter the new video link.:")
        videos[index-1]= {'name':name,'time':time}
        helper(videos)
    else:
        print("Invalid input.")

def add_video(videos):
    name = input("Enter name of video.:")
    time = input("Enter duration of video.:")
    link = input("Paste link of video.\n")
    videos.append({'name':name,'time': time,'link':link})
    helper(videos)
def list_of_videos(videos):
     for index,point in enumerate(videos,start=1):#ham yaha enumerate isliye ue kar rahe h kyuki hamko yaha pe video ki indexing chaiye
          print("-"*180)
          print(f"{index}.{point['name']}\nDuration:{point['time']}\nLink:{point['link']}")
         
def main():
    videos= load_data()
    while True:
        print("*"*180)
        print("Youtube Manager")
        print("1. List of videos.")
        print("2. Add video.")
        print("3. Update previous video.")
        print("4. Search a video using ID of video.")
        print("5. Delete a video using ID of video.")
        print("6. Exit")
        print("*"*180)
        choice = input("Enter a choice.:")
        
       
        
        match choice:
            case '1':
                list_of_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                Update_video(videos)
            case '4':
                search_video(videos)
            case '5':
                delete_video(videos)
            case '6':
                break
            case _:
                print("Invalid choice.")


if __name__ == "__main__":
    main()