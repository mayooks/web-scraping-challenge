# web-scraping-challenge
In this work I build a flask web application that scrapes four websites for data related to Mars planet and displays the information in a single HTML page. 


The app finds the most recent mars news title and content from 
 <ul>
  <li>4 full-resolution hemisphere image from <a href="https://marshemispheres.com/">marshemispheres</a></li>
  <li>Featured Image from <a href = "https://spaceimages-mars.com/">spaceimages-mars</a></li>  
  <li>Mars planet latest headlines <a href= "https://redplanetscience.com/">redplanetscience</a></li>
  <li>Mars planet facts from a table from <a href= "https://galaxyfacts-mars.com/">galaxyfacts-mars</a></li>
</ul>   

The app works by  creating routes for index and scraping, establishing MongoDB connection, correctly rendering template to HTML, and properly calling the scraping method from an external python module. The user can aupdate the content displayed on the up by clicking on the Get Data button displayed on the top of the images
