import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point

def create_polygon(coordinates):
    """
    Given a list of lat, lon coordinates, return a Polygon
    """
    assert type(coordinates)==list, "Not a list"
    points = [(point['lng'], point['lat']) for point in coordinates]
    try:
        polygon = Polygon(points)
        return polygon
    except:
        print("Couldn't create a Polygon from the coordinates")
        return None
    
def get_centroid(polygon):
    """
    Given a Polygon object, return Point centroid
    """
    centroid = polygon.centroid
    # centroid_x, centroid_y = centroid.x, centroid.y
    # return centroid_x, centroid_y
    return centroid


def plot_polygon(coordinates):
    # Plotting the polygon
    polygon = create_polygon(coordinates)
    x, y = polygon.exterior.xy
    plt.figure(figsize=(10, 10))
    plt.plot(x, y)
    plt.fill(x, y, alpha=0.3)
    plt.title("Polygon from Lat/Lon Coordinates")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.axis('equal')
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def get_centroid_coordinates(polygon):
    """
    Return the lat, lon (in that order) coordinates of the centroid of the polygon object.
    Note: shapely Polygon object follows the convention that x is lat and y is lon
    """
    centroid = polygon.centroid
    lat, lon = centroid.y, centroid.x
    return lat, lon


def plot_polygon_and_centroid(coordinates):
    # Plotting the polygon
    polygon = create_polygon(coordinates)
    x, y = polygon.exterior.xy
    plt.figure(figsize=(10, 10))
    plt.plot(x, y)
    plt.fill(x, y, alpha=0.3)
    plt.title("Polygon from Lat/Lon Coordinates")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.axis('equal')
    plt.grid(True)
    #plot centroid
    centroid = polygon.centroid
    plt.plot(centroid.x, centroid.y, 'ro') 

    plt.tight_layout()
    plt.show()

