import requests, os

class ImageSourcer:

    # Constructor initialising attributes
    def __init__(self, rover, sol, camera, index):
        apiKey = "lORFMg7rox7XMLBWzM1byE9fd5WAe3Cf9KkoQYmp"
        self.rover = rover
        self.sol = sol
        self.camera = camera
        self.responseString = ("https://api.nasa.gov/mars-photos/api/v1/rovers/" + self.rover + "/photos?sol="
                               + self.sol + "&camera=" + self.camera + "&api_key=" + apiKey)
        self.index = index

    def __call__(self):
        return (self.index)

    # Write links to images to text file
    def writeToFile(self, data, fileName):
        textFile = open(fileName, "w")
        for entry in data["photos"]:
            print(entry["img_src"])
            textFile.write(entry["img_src"])
            textFile.write("\n")

    def returnURL(self, data):
        return data["photos"][self.index]["img_src"]

    # Send API request for JSON object
    def receiveImages(self):
        response = requests.get(self.responseString)

        # Check to see if request OK
        if (response.status_code != 200):
            print ("API Request failed")
        else:
            data = response.json()

            # Create file name and store in folder 'images'
            fileName = self.rover + "-" + self.sol + ".txt"
            completeFileName = os.path.join("images/", fileName)

            # Remove file if already exists for parameters, to allow new data
            # to be retrieved
            if (os.path.isfile(completeFileName)):
                os.remove(completeFileName)
            else:
                return self.returnURL(data)
