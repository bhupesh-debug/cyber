import os
import sys
import math
import json
import urllib.request
from datetime import datetime
import pandas as pd
from PIL import Image, ImageDraw

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable, Image as RLImage
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

BASE_DIR = r"C:\Users\bhupe\Downloads\Backend\cyber\GPS_Address_Intelligence"
MAPS_DIR = os.path.join(BASE_DIR, "maps")
VERIF_DIR = os.path.join(BASE_DIR, "verification")
os.makedirs(MAPS_DIR, exist_ok=True)
os.makedirs(VERIF_DIR, exist_ok=True)

LAT = 33.4413
LON = -112.0421
SAMPLE_ID = "GEO-2026-135-01"

# Load cached data if available
nom_path = os.path.join(VERIF_DIR, "raw_nominatim.json")
if os.path.exists(nom_path):
    with open(nom_path, "r", encoding="utf-8") as f:
        nom_data = json.load(f)
else:
    nom_data = {}

census_path = os.path.join(VERIF_DIR, "raw_census.json")
if os.path.exists(census_path):
    with open(census_path, "r", encoding="utf-8") as f:
        census_data = json.load(f)
else:
    census_data = {}

address_obj = nom_data.get("address", {})
street = address_obj.get("road", "East Sky Harbor Circle North")
suburb = address_obj.get("suburb", "Central City")
city = address_obj.get("city", "Phoenix")
county = address_obj.get("county", "Maricopa County")
state = address_obj.get("state", "Arizona")
zip_code = address_obj.get("postcode", "85034")
country = address_obj.get("country", "United States")
country_code = address_obj.get("country_code", "us").upper()
formatted_address = nom_data.get("display_name", "East Sky Harbor Circle North, Central City, Phoenix, Maricopa County, Arizona, 85034, United States")

census_geos = census_data.get("result", {}).get("geographies", {})
census_tract = census_geos.get("Census Tracts", [{}])[0].get("NAME", "Census Tract 1139") if census_geos.get("Census Tracts") else "Census Tract 1139"

map_img_path = os.path.join(MAPS_DIR, "map_snapshot.png")

# Palette tokens
C_NAVY = colors.HexColor("#14243A")
C_CHARCOAL = colors.HexColor("#252B33")
C_GOLD = colors.HexColor("#B49A62")
C_SILVER = colors.HexColor("#A7ADB5")
C_IVORY = colors.HexColor("#F7F5EF")
C_MUTED_BLUE = colors.HexColor("#647C91")
C_WARM_GRAY = colors.HexColor("#E8E5DD")
C_GREEN = colors.HexColor("#15803D")

class IntaglioEngravingCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(IntaglioEngravingCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_intaglio_artwork(num_pages)
            super(IntaglioEngravingCanvas, self).showPage()
        super(IntaglioEngravingCanvas, self).save()

    def draw_guilloche_corner(self, xc, yc, r_out=22, r_in=7, d=11, loops=4):
        p = self.beginPath()
        steps = 120
        first = True
        for i in range(steps + 1):
            t = (i / steps) * (2 * math.pi * loops)
            x = xc + (r_out - r_in) * math.cos(t) + d * math.cos((r_out - r_in) / r_in * t)
            y = yc + (r_out - r_in) * math.sin(t) - d * math.sin((r_out - r_in) / r_in * t)
            if first:
                p.moveTo(x, y)
                first = False
            else:
                p.lineTo(x, y)
        self.drawPath(p, stroke=1, fill=0)

    def draw_watermark_rosette(self, xc, yc, r=130):
        self.saveState()
        self.setStrokeColor(colors.HexColor("#E2DCCE"))
        self.setLineWidth(0.35)
        # Symmetrical radial coordinate rings
        for rad in range(30, r, 20):
            self.circle(xc, yc, rad, stroke=1, fill=0)
        # Compass rays
        for deg in range(0, 360, 15):
            rad_angle = math.radians(deg)
            x1 = xc + 25 *