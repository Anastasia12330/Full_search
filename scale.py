

def scale_object(coodrinates_object, coodrinates_Corner):
    toponym_longitude, toponym_lattitude = coodrinates_object.split(" ")
    delta_l = round(float(toponym_longitude) - float(coodrinates_Corner.split(' ')[0]), 4)
    delta_r = round(float(toponym_lattitude) - float(coodrinates_Corner.split(' ')[1]), 4)

    return str(delta_l), str(delta_r)
