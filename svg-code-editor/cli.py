import click
# from os import system

@click.command()
@click.argument("input", type=click.File("r"))
def cli(input):
    # this:
    # <path d="M311.111 420H288.889V455.556V468.889H311.111V455.556V420Z" fill="#695A69"/>
    # needs to turn into this:
    # <path d="M311.111 420H288.889V455.556V468.889H311.111V455.556V420Z" stroke="#B2441D" stroke-width="2px" class="color-1" />

    # need to choose a color for the stroke (this is has nothing to do with the fill color)

    # need to choose a width for the stroke (article choose 2px going to go with that)

    # then take the color inside fill and for each unique one put it into a list

    # assign each color inside of list to a class of it's own by incrementing each time we find a unique color

    # within each <path> we need to get rid of the fill="####" 
    # (which is also 2nd fill to the end of the file)
    # for each unique fill we will add it to a list
    # then with that list we will make a css class for each
    # if line contains <path and fill
    # 

    # get all the lines inside of input file and assign them to lines
    lines = input.readlines()        
    # outlineColor = "#B2441D"
    # TODO allow user input to determine this
    outlineColor = "#080707"
    # will hold colors found within svg
    colorsList = []
    # the name of the file before the extension
    beforeExtension = input.name[0:input.name.find(".")]
    # creating new file to write our new svg code
    # input/parameter file is already opened for reading
    with open(f"{beforeExtension}-new-code.txt", "w") as newFile:
        # loop through each line within input file
        for line in lines:
            # if current line contains path
            if line.find("path") != -1:
                fillAttr = line.find("fill=\"") - 1
                startColor = fillAttr + 7
                endFillAttr = line.find("\"", startColor)
                colorStr = line[startColor:endFillAttr]

                if not doesItemExist(colorsList, colorStr):
                    colorsList.append(colorStr)
                newFile.write(f"{line[0:fillAttr]} stroke=\"{outlineColor}\" stroke-width=\"2px\" class=\"color-{colorsList.index(colorStr) + 1}\"/>\n")
            # line did not contain path, simply re-write it
            else:
                newFile.write(line)
    # write css rules
    with open(f"{beforeExtension}-js.txt", "w") as js:
        for index, color in enumerate(colorsList):
            js.write(f"fillPath(\"color-{index + 1}\", \"{color}\");\n")

def doesItemExist(colorsList, color):
    for x in colorsList:
        if x == color:
            return True
    return False