Script is using weatherstack.com site to check current day weather status, in detail it's checking uv index and chance
of the rain. If uv index is greater than 3 then this is the trigger for taking sunscreen, if chance of the rain is greater than
5 percent then this is the trigger for taking umbrella with me.

On first we are checking our local city for which we want to check weather status. Then we are checking current date.
With those arguments we are sending http request to weatherstack.com to get uv index and chance of the status.

We also want that script is automatically trigger each day at 6 am, for this case we will use crontab.

Script is containerized with Docker. Also one bash script is created for starting docker container with script that has
two different arguments rain and shine. This script will be put into the crontab for execution each day at 6 am

Steps for starting Docker and putting script in Crontab

1. Position yourself in the terminal in the folder where script and Dockerfile are stored
2. Create docker image -> docker build -t weather_image .
3. To check if the script is working well execute this command -> bash run_docker shine
4. To put script in the crontab first you need to edit cron jobs -> crontab -e
5. Add shine entry for script -> 0 6 * * * /path/to/run_docker.sh shine
6. Add rain entry for script -> 0 6 * * * /path/to/run_docker.sh rain
