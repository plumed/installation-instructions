#!/bin/bash

./generate_installation_page > InstallationPP.md
python build_full_graph.py
