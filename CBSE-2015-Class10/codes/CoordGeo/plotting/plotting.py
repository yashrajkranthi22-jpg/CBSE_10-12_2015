"""Drawing helpers for coordinate-geometry diagrams.

The helpers use Matplotlib as the drawing backend, while keeping common
geometric constructions (segments, points, circles, arcs, and polygons)
inside the bundled CoordGeo library.
"""
from matplotlib.patches import Arc, Circle, Polygon, Rectangle, Wedge


def plot_line(ax, start, end, **style):
    """Draw the straight segment joining two (x, y) points."""
    return ax.plot([start[0], end[0]], [start[1], end[1]], **style)


def plot_curve(ax, x_values, y_values, **style):
    """Draw a curve from its x- and y-coordinate values."""
    return ax.plot(x_values, y_values, **style)


def plot_points(ax, points, **style):
    """Draw a collection of (x, y) points."""
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    return ax.scatter(x_values, y_values, **style)


def plot_label(ax, x, y, text, **style):
    """Place a label at the requested coordinate."""
    return ax.text(x, y, text, **style)


def annotate(ax, text, xy, xytext, **style):
    """Add a label with an optional arrow pointing to a coordinate."""
    return ax.annotate(text, xy=xy, xytext=xytext, **style)


def add_circle(ax, centre, radius, **style):
    """Draw a circle with the given centre and radius."""
    shape = Circle(centre, radius, **style)
    ax.add_patch(shape)
    return shape


def add_arc(ax, centre, width, height, **style):
    """Draw an elliptical arc centred on a coordinate."""
    shape = Arc(centre, width, height, **style)
    ax.add_patch(shape)
    return shape


def add_polygon(ax, points, **style):
    """Draw a polygon through an ordered list of coordinates."""
    shape = Polygon(points, **style)
    ax.add_patch(shape)
    return shape


def add_wedge(ax, centre, radius, theta1, theta2, **style):
    """Draw a circular sector from angle theta1 to theta2 (in degrees)."""
    shape = Wedge(centre, radius, theta1, theta2, **style)
    ax.add_patch(shape)
    return shape


def add_rectangle(ax, xy, width, height, **style):
    """Draw a rectangle from its lower-left coordinate, width, and height."""
    shape = Rectangle(xy, width, height, **style)
    ax.add_patch(shape)
    return shape


def fill_polygon(ax, x_values, y_values, **style):
    """Fill a polygon supplied as separate x- and y-coordinate lists."""
    return ax.fill(x_values, y_values, **style)
