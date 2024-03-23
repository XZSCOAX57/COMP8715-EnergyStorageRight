Table of Contents
=================
  * [Status](#Status)
  * [Introduction](#Introduction)
  * [Vision](#Vision)
  * [Main features](#Main-features)
  * [Deliverables](#Deliverables)
  * [Desired Features](#Desired-Features)
  * [The potential of the project](#The-potential-of-the_project)
  * [Acknowledgement](#Acknowledgement)
  * [Work allocation](#work-allocation)
  * [Link to Documentation](#Link-to-Documentation)
  * [Link to Webserver](#Link-to-Webserver)
  * [Other Readme resources](#Other-Readme-resources)
  ## Project Management
  * [Decision Log](https://github.com/users/XZSCOAX57/projects/1)
  * [Milestones](https://github.com/users/XZSCOAX57/projects/4)
  * [Reflection Log](https://github.com/users/XZSCOAX57/projects/2)
  * [Risk Log](https://drive.google.com/drive/folders/1tSDZvzWGLMqH99RsNxV9itQPNsYYlvM2?usp=drive_link)
  * [Stakeholder](https://drive.google.com/drive/folders/1ZtMsAejGNsbLj8_JLwOPAK1YXPbdcp1T?usp=drive_link)
  * [Meeting Agendas](https://drive.google.com/drive/folders/1I3LaH8eNgUA0kkkIxVkLKdnRlQfhQX_c?usp=drive_link)



## Status

The previous EnergyStorageRights development team has built a user-friendly web application designed to help companies increase their profits by pinpointing the best places to get the most abundant energy. The web application will support users in selecting their favorite areas either through automated processes or manual controls via a user-friendly panel.
However, the site has some lingering issues stemming from previous development phases. Our primary focus lies in resolving these lingering concerns left behind by the previous team. One of the highest priority of these legacy issues is on the construction of the PHES module. Furthermore, we aim to enhance the user experience and explore potential avenues for refining algorithmic quality and datasets.

## Introduction
Deployment of renewable energy technologies in a different location often comes with advantage and disadvantage. The energy storage rights is a digital platform that will map, evaluate, promote and help investments in the development rights for energy storage pilot projects such as pumped hydro energy storage, floating solar pilots on lake or sea. Alongside with the platform is energy storage rights application.

We strike to build up an application which used to evaluate and optimize the performance and potential of location viable for development of different renewable-energy technologies, this outcome will then be visualized to the target user.

Through our development on this project, we use Google drive for documentation purposes and data storage. Trello for task management and assignment. The links can be found in [Link to our other resources](#Link-to-our-other-resources).


## Main features

* **Visualize the energy distribution gloabal wide in the website**
* **Allow user to see the potential energy output from implementing renewable technologies in the desire location**
* **Energy output can be calculated by single point or polygon area**
* **Allow variation when calculating potential energy output using different attribute (energy price, hardware specification, etc.)**
* **Predict potential energy output using data that not involve in the equation (e.g. tempurature) instead of correlated data (e.g. solar irradiation)**
## System Architecture
# ![image](https://github.com/tudorelu/energy_storage_rights/blob/master/Documents/System%20Architecture.png)

## Deliverables
### Stage 1:Web Server Deployment (Semester 1 Week 6 & Second Audit)
#### Introduction
By dividing the tasks into these two stages, the team can first ensure that the application is stable, secure, and offers a basic user experience on the web server. The second stage then focuses on refining the PHES model, adding advanced features, and optimizing performance. This stage focuses on deploying the application onto the web server, ensuring the application's stability, security, and basic user experience to remain the same as the offline version.
#### Deliverables
#### Back-end Group
* **Integrate functional methods into main method. Integrate the code of different branches, and potential risks and potential   issues encountered**
* **Find a server and deploy our MVP on it. Make our MVP a usable website to ensure the application's stability, security, and basic user experience to remain the same as the offline version.**
* **Data managerment. Because our data volume is relatively large, we need to find a reasonable way to store our data.**
* **PHES Module I . Because the existing cost model is a basic one, we will try to explore a new way to make the cost model more flexible under the new needs of users. For example, we consider pipeline costs for the shortest straight-line distances, but the reality can 
#### Front-end Group
* **Web Server I. Web server testing, comparison, and selection. Research & find an appropriate web server for backend usage.**
* **Integration of PHES modules I. Assist back-end members with integration and testing of PHES modules.**
* **User interface design research and improvement. A more user-friendly UI plan is refined. Self-review previous UI structure, and develop and improve the information panel.**  
### Stage 2: Advanced Enhancements and Detailed Development (Semester 1 Week 10 & Final Audit)
#### Introduction
This stage focuses on refining the user experience, adding advanced features, including PHES model and cost model and potential 3D map and further optimizations.
#### Deliverables
#### Back-end Group
* **Research on Cost Model. Adding quotes for different units to the revised Cost Model. Because the information about the user's demand contains various combinations, such as 1500GWh 504h or 500GWh 168h, these additional demands should also be considered after the revised model has been worked out.**
* **Integration and Test Algorithms II. Test Cost Model to see if it can accommodate different units of inputs.**
* **PHES Module II. Examine the methodology and explore if there are options for improvement**
#### Front-end Group
* **Web Server II. Web server testing, comparison, and selection. Research & find an appropriate web server for backend usage**
* **Integration of PHES modules II. Assist back-end members with integration and testing of PHES modules.**
* **Research on 3D maps. Our current website can only be displayed on a 2D map, exploring the possibility of replacing the map with a 3D one.**


## Desired Features
Our final product is desired to have some other functions. The application should be able to identify the top N locations that are suitable for development in a relatively large area. To rank different locations, we will continue to use the return of investment as the parameter.<br />
On the other hand, the application should be able to select a combination of different technologies where it yields most energy output.

## Milestones
Refer to [Link](https://github.com/users/XZSCOAX57/projects/4)

## The potential of the project
Many potential users are interested in renewable energy, our application can help to identify the high potential area for developing renewable energy. This allows for generating more interaction between the property owner and the renewable energy developer. The landowner can benefit from this application by making a more effective and smart decision on the use of renewable energy product, it also helps them to reduce the spending in energy, increase in efficiency in energy storage. For the renewable energy developer, it grants them more opportunity to develop their products. This application is expected to create a win-win situation between each party.

## Acknowledgement
This project is carried out under computing project courses including COMP3500, COMP4500, and COMP8715 from The Australian National University. This project team is led by project manager Peilin Liu(u7518297@anu.edu.au) and consist five other team members, Ziyang Wu(u6262265@anu.edu.au), Zhengshi Xie(u7503941@anu.edu.au),  Derek Huang(u7300484@anu.edu.au), Zhengyu Chen(u7531371@anu.edu.au), and Jingbin Lin(u7664372@anu.edu.au).

## Work allocation
|Role|Principle|Vice|Assistant|
|--------|------|--------|--------|
|Project Manager| Peilin Liu| Zhengshi Xie|
|Product Manager | Zhengyu Chen|
|Spokesman| Zhengshi Xie | Peilin Liu|
|Recorder| Peilin Liu | Zhengshi Xie | Derek Huang|
|Back-end| Ziyang Wu| Zhengshi Xie |
|Front-end| Peilin Liu | Derek Huang | Jingbin Liu|

## Link to Documentation
[Website](http://54.89.36.221:8000/) <br/>
[Google doc](https://drive.google.com/drive/folders/1Bkb0iNbjvN38zyL3I1o1o8QEcVQbB9Ik?usp=sharing) <br/>
[Meeting Agendas](https://drive.google.com/drive/folders/1I3LaH8eNgUA0kkkIxVkLKdnRlQfhQX_c?usp=drive_link)<br/>
[Decision Log](https://drive.google.com/drive/folders/11Do3tRJSuvCfOn7xhhx_bhmt9q6lyAY5?usp=drive_link)<br/>
[Reflection](https://drive.google.com/drive/folders/1rMfFTu1qsl83mC_qMsC0Lwq-KMRrusmt?usp=drive_link)<br/>
[Risk Register](https://drive.google.com/drive/folders/1tSDZvzWGLMqH99RsNxV9itQPNsYYlvM2?usp=drive_link)<br/>
[Milestone]( https://github.com/users/XZSCOAX57/projects/4  )<br/>
[Trello page](https://trello.com/invite/userworkspace81642725/ATTI6037f730b55bdb7fec67918199b672c05D08580F)https://trello.com/invite/userworkspace81642725/ATTI6037f730b55bdb7fec67918199b672c05D08580F<br/>

## Link to Webserver
[Website]( https://propane-net-292307.ts.r.appspot.com/)<br/>
