#!/bin/bash

if [[ "$1" == "rain"]]; then
  docker run --name weather_container weather_image python main.py rain
elif [[ "$1" == "shine"]]; then
  docker run --name weather_container weather_image python main.py shine
else
  echo "Invalid option provided."
fi
