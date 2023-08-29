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
  * [Milestones](#Milestones)
  * [Reflection Log](https://github.com/users/XZSCOAX57/projects/2)
  * [Risk Log](https://docs.google.com/document/d/19IOad0_Ua6MBCcvc2Y1iHC4XGMy_Vs_O/edit?usp=drive_link&ouid=112330158341239860556&rtpof=true&sd=true)
  * [Stakeholder](https://docs.google.com/document/d/1YDbaIrAVe7zR38DHSNd55uN4sTgGQPE0/edit?usp=drive_link&ouid=112330158341239860556&rtpof=true&sd=true)
  * [Meeting Agendas](https://drive.google.com/drive/folders/1u-J-U2CourcMfQXPsqqY9ymTFHw-hAev)



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
### Stage 1:Critical Fixes and Basic Enhancements (Semester 1 Week 6 & Second Audit)
#### Introduction
This stage focuses on addressing the most critical issues, ensuring the application's stability, security, and basic user experience.
#### Deliverables
#### Back-end Group
* **Uniform API Response Formats (Implement a basic authentication system to secure the API endpoints.)**
* **Remove Unused API Endpoints (Identify and remove any redundant routes or functions.)**
* **API Authentication I (Implement a basic authentication system to secure the API endpoints.)
* **PHES Module I (Understanding the Principles of PHES Modules)**
#### Front-end Group
* **HTML5 Keywords (Update any deprecated or old-version-specific keywords.)**
* **Basic Error Handling (Implement basic error handling for common issues, such as failed data fetches.)**
* **HI-FI Prototype (Develop a detailed and interactive prototype using Mockplus for user experience research.)**
* **LO-FI Prototype (Sketch out the basic design and flow of the application on paper.)**

### Stage 2: Advanced Enhancements and Detailed Development (Semester 1 Week 10 & Final Audit)
#### Introduction
This stage focuses on refining the user experience, adding advanced features, and further optimizations.
#### Deliverables
#### Back-end Group
* **Advanced API Authentication (Enhance the authentication system with features like token refresh, blacklisting, and more fine-grained access controls.)**
* **Optimisation of data storage methods (At this stage the amount of data used is large and the data is stored locally, try using an online database.)**
* **PHES Module II (Examine the methodology and explore if there are options for improvement.)**
#### Front-end Group
* **Advanced Error Handling (Implement more advanced error handling mechanisms, such as retry mechanisms for failed requests or user feedback systems for reporting issues.)**
* **Security Protection for CSV (Implement basic security measures for sending CSV data.)**
* **Function Development (Develop the Home page showcase, Map loading, and Help/contact document showcase features.)**

### Long-term plans
#### Introduction
There are no exact delivery times for the long term plans as these will always be in place throughout the timeline of our projects.
#### Deliverables
* **Advanced Performance and Caching (Profile the application to identify areas for further optimization；Implement advanced caching mechanisms on both the client and server sides；Optimize heavy computations and consider offloading them to background tasks if necessary)**
* **Separate Front-end and Back-end Code (Begin the process of separating the codebases into distinct directories.
)**

## Desired Features
Our final product is desired to have some other functions. The application should be able to identify the top N locations that are suitable for development in a relatively large area. To rank different locations, we will continue to use the return of investment as the parameter.<br />
On the other hand, the application should be able to select a combination of different technologies where it yields most energy output.

## Milestones
Refer to [Gantt Chart](https://github.com/tudorelu/energy_storage_rights/blob/master/Documents/Gantt%20Chart.xlsx)

## The potential of the project
Many potential users are interested in renewable energy, our application can help to identify the high potential area for developing renewable energy. This allows for generating more interaction between the property owner and the renewable energy developer. The landowner can benefit from this application by making a more effective and smart decision on the use of renewable energy product, it also helps them to reduce the spending in energy, increase in efficiency in energy storage. For the renewable energy developer, it grants them more opportunity to develop their products. This application is expected to create a win-win situation between each party.

## Acknowledgement
This project is carried out under computing project courses including COMP3500, COMP4500, and COMP8715 from The Australian National University. This project team is led by project manager Peilin Liu(u7518297@anu.edu.au) and consist six other team members, Yuli Lin(u5927759@anu.edu.au), Ziyang Wu(u6262265@anu.edu.au), Zhengshi Xie(u7503941@anu.edu.au), Boyang Zhang(u7528692@anu.edu.au), Derek Huang(u7300484@anu.edu.au), Zhengyu Chen(u7531371@anu.edu.au).

## Work allocation
|Role|Principle|Vice|Assistant|
|--------|------|--------|--------|
|Project Manager| Peilin Liu| Boyang Zhang|
|Product Manager | Zhengyu Chen|
|Spokesman| Zhengshi Xie | Peilin Liu|
|Recorder| Peilin Liu | Zhengshi Xie | Derek Huang|
|Back-end| Ziyang Wu| Zhengshi Xie | Yuli Lin|
|Front-end| Peilin Liu | Boyang Zhang | Ziyang Wu|

## Link to Documentation
[Website](https://propane-net-292307.ts.r.appspot.com/) <br/>
[Google doc](https://drive.google.com/drive/folders/1k5dIK1WhgznQoBR5lxQIU7OrqCI_OeCf) <br/>
[Meeting Agendas](https://drive.google.com/drive/folders/1lbQkP5mrmUKXxlAF_FvXwwWyoZpDpv8R)<br/>
[Algorithm Document]( https://drive.google.com/drive/folders/1ZyEXnGx5kGcSUAVw1QPgWDjQdaQ5DUON?usp=share_link)<br/>
[Data Research](https://drive.google.com/drive/folders/12mnskEiLVKCq8pss-6izwgLr6nEDkFq0?usp=share_link  )<br/>
[Decision Log]( https://github.com/users/XZSCOAX57/projects/1  )<br/>
[Reflection](https://github.com/users/XZSCOAX57/projects/2 )<br/>
[Risk Register]( https://drive.google.com/drive/folders/1XYEa8MV4klCDVyCWnQFCGeZhQz6f1vuU?usp=share_link)<br/>
[[Milestone]( https://github.com/users/XZSCOAX57/projects/4  )<br/>
[Trello page]( https://trello.com/b/kCYjanpm/links-with-project  )<br/>

## Link to Webserver
[Website]( https://propane-net-292307.ts.r.appspot.com/)<br/>

## Other Readme resources
### Master Branch
[Master](https://github.com/tudorelu/energy_storage_rights)<br />
[Algorithm Document](https://github.com/tudorelu/energy_storage_rights/tree/master/Documents/Algorithm%20Documents)<br />
[Code](https://github.com/tudorelu/energy_storage_rights/tree/master/Code)<br />
[Code/Testing](https://github.com/tudorelu/energy_storage_rights/tree/master/Code/Testing%20on%20sample%20algorithm)<br />
[Code/data](https://github.com/tudorelu/energy_storage_rights/tree/master/Code/data)<br />
[Data Research](https://github.com/tudorelu/energy_storage_rights/tree/master/Data%20Research)<br />
[Progress](https://github.com/tudorelu/energy_storage_rights/tree/master/Progress)<br />
[To Do List App](https://github.com/tudorelu/energy_storage_rights/tree/master/To%20Do%20list%20App)<br />

### Web Branch
[Web](https://github.com/tudorelu/energy_storage_rights/tree/Web)<br />
[Large Data File](https://github.com/tudorelu/energy_storage_rights/tree/Web/Large%20Data%20File%20To%20Create%20Layers)<br />
[Basic Arcgis](https://github.com/tudorelu/energy_storage_rights/tree/Web/basic-arcgis)<br />
