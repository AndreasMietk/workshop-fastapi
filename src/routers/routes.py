import json

from fastapi import APIRouter, HTTPException
from fastapi import FastAPI, Request, Form
from starlette.responses import HTMLResponse
import osmnx
import networkx
from osmnx._errors import InsufficientResponseError

from src.models.routes import Route
from src.templates import jinja_templates, render_template

routes_router = APIRouter(prefix="/routes")

@routes_router.get('')
@routes_router.get('/')
def index(request: Request):
    return jinja_templates.TemplateResponse(request=request, name="routes_list.html")


@routes_router.post('')
@routes_router.post('/')
def store(request: Request, route_name: str = Form(...), route: str = Form(...)):
    try:
        route_coordinates = json.loads(route)

        route = Route()
        route.coordinates = route_coordinates
        route.name = route_name

        # Implement your storage logic here
        return f"Nice Route, but implement me! {route.__repr__()}"
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=400, detail="Invalid JSON format")


@routes_router.get('/{route_id}')
def show(request: Request, route_id: str):
    pass


@routes_router.post('/plan', response_class=HTMLResponse)
async def plan_route(request: Request, start: str = Form(...), end: str = Form(...)):
    # Convert start and end locations to tuples of floats
    try:
        start_coords = tuple(map(float, start.split(',')))
        end_coords = tuple(map(float, end.split(',')))

        # Swapping the first and second elements
        start_coords = (start_coords[1], start_coords[0])
        end_coords = (end_coords[1], end_coords[0])
    except ValueError:
        return render_template('index.html', request=request, error="Invalid coordinates format. Please try again.")

    try:
        # Download the graph
        G = osmnx.graph_from_point(start_coords, dist=2000, network_type='bike')

        # Get the nearest nodes to the start and end points
        orig_node = osmnx.nearest_nodes(G, start_coords[1], start_coords[0])
        dest_node = osmnx.nearest_nodes(G, end_coords[1], end_coords[0])

        # Find the shortest path
        route = networkx.shortest_path(G, orig_node, dest_node, weight='length')

        # Get the coordinates of the route
        route_coords = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in route]

        return render_template('index.html', request=request, route=route_coords, start=start, end=end)
    except InsufficientResponseError:
        return render_template('index.html', request=request,
                               error="No data available for the selected points. Please try again with different points.")
    except Exception as e:
        return render_template('index.html', request=request, error=f"An error occurred: {str(e)}")

