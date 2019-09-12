#!/usr/bin/python3
from models import storage
from api.v1.views import app_views
from flask import Flask, Blueprint, make_response, jsonify, request
from os import getenv
from flask_cors import CORS
