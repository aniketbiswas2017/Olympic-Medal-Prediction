XXX-X-XXXX-XXXX-X/XX/$XX.00 ©20XX IEEE
VISUALIZING OLYMPICS
Uday Sharma Masters of applied computer science Dalhousie university Halifax, Canada
B00781179 ud836628@dal.ca
Aniket Biswas Masters of applied computer science Dalhousie university Halifax, Canada
B00781091 an584252@dal.ca
Kunal Sharma Masters of applied computer science Dalhousie university Halifax, Canada
B00780464 kn781914@dal.ca
Abstract— This report explores the hypothesis that the number of medals won by a country in the Olympic games is dependent on the population, GDP per capita, human development index (HDI), number of internet users and number of athletes representing the country. The graphs also represent the performance the countries in the Olympics history based on the gender ratio of the respective teams and the effects of being the host nation. This project report provides an application overview of the visualization
components and the conclusions derived from the respective visualizations.
I. INTRODUCTION
Every four years, the Olympic games are witnessed by the world. Over 220 million Americans watched the Rio 2016 summer Olympics and celebrated as their country won 121 medals. That’s 51 more medals than the second-place winner, China
(70), and 54 more than the third-place winner, Great Britain (67). However, this is not always the case. The varied dynamics associated with a country's Olympics dominance is dependent on the attributes that are hidden form the spectators. Our project uses Olympics data from all the Olympic games till date to understand the factors that affect a country's performance in the games. The following is a list of key attributes we considered while analyzing a nation's Olympic performance:Gross domestic production per capita, Number of Internet Users, National Population, Games’ Host City, Number of Participating Athletes, Distance of country's capital from the equator
These attributes are the core of our data visualization analysis. We chose to focus on summer Olympics because it has much larger participation percentage than the winter Olympics.
II. MOTIVATION
Olympics data has been available ever since the first recorded games and its exponential growth gives us the motivation to study the key elements that drive a nation to excellence in the games. The factors behind the success go un-noticed by the
spectators and we attempt to visualize some interesting facts based on the historical performances.
III. DATASET SOURCES
(i) GDP per capita
Description: This dataset lists the GDP per capita, total population of internet users and HDI of the participating countries from the year 1896 to 2016.
Data Source: https://data.worldbank.org/indicator/NY.GDP.PCAP.CD
(ii) All time Olympic medals won by countries in respective games
Description: This dataset lists the medals won by the countries in the respective events and the gender of the athletes.
Data Source: https://www.kaggle.com/jeffksw/olympics-history-medals/data
IV. DATA VISUALIZATIONS
The following sections explains the nine data visualizations contained in our project. Each visualization outlines the motivation behind selecting the visualization and information being presented to the users.
1. Interactive Parallel Co-ordinates Plot
• To represent each Country along with their respective medal tally in respective Events.
• Data provided is for Rio Olympics (Summer) 2016.
• Multiple countries can be selected, reset to find their corresponding Event or rivalry.
• Simple and interactive way to represent each country and sports side by side.
Fig. 1. Interactive Parallel Co-ordinates Plot
2. Simple Bar chart
• Shows the count of Gold medals won by the top 30 countries for Olympics 2016
• On the x-axis is the Top 30 countries and on the y-axis, is the number of medals.
• Country list is sortable according to descending order of count of medals or alphabetically.
• Automatically sorts on start-up according to the descending order of medal count.
Fig. 2. Simple Bar Chart
3. Complex Bar chart
• Shows the total count of all medals won by the top 40 countries for Olympics 2016
• On the x-axis is the Top 40 countries and on the y-axis, is the number of medals.
• Integrated performance of both Winter Olympics and Summer Olympics to check any co-relation.
• Stacked chart of gold, silver, bronze and total medals to represent in one graph.
Fig. 3. Complex Bar Chart
4. World Globe (Choropleth)
• Shows all countries to have ever participated in the Summer Olympics till date.
• Uses ‘topojson’, ‘geo.orthographic’ and transition feature – interpolate method.
• This was chosen to give a more aesthetic visualization feel to the website created.
• The name of the country is highlighted on the right side of the screen as the globe rotates.
Fig. 4. World Map (in form of globe) [Choropleth]
5. Stacked Bar chart
• Shows the total medal count of the top 50 countries for Olympics since the beginning of time.
• On the x-axis is the is the number of medals and on the y-axis, is the Top 50 countries.
• Bar chart shows the corresponding medals in their respective colours.
6. Steam Graph
• Shows the total medal count of the top 10 countries for Olympics since the beginning of time.
• It corelates the difference of medals according to the gender of athletes.
• It also highlights the increasing participation of women athletes over time.
• The series can hover interactively based on the year on the x-axis and country based on colour.
• An obvious trend in observed in the visualization about the growing women participation.
• It uses d3 sankey plugin , d3 sankey chart.
Fig. 5. Steam Graph. (Men Medallists)
Fig. 6. Steam Graph. (Women Medallists)
7. Stacked Bar chart
• Shows the total medal count by gender of all countries in the Olympics since the beginning of time.
• On the x-axis is the years from 1896 to 2006 and on the y-axis, is the count of medals.
• Colour wise differentiation is observed for gender and on hover.
Fig. 7. Stacked Bar Chart. (Gender)
8. Interactive Olympic Rings
• Shows the 5 colour Olympic rings created using javascript.
• Mainly chosen for aesthetic feel for website and creative visualization.
Fig. 8. Olympic Rings
9. Interactive Line chart
• Shows the performance of host countries by year, their rankings and medal counts.
• On the x-axis is the years from 1896 to 2012 and on the y-axis, is the count.
• Tooltip can be used to select the Rank and various medals to visualize a particular graph.
• Years on the x-axis can be highlighted to view a particular year and its host.
• On the extreme right, a country or glyph can be highlighted to view its performance.
Fig. 9. Interactive Line Chart
V. MACHINE LEARNING APPROACH
The above-mentioned datasets are used to input the data for machine learning approach.
Phase 1. Data Preprocessing
The following steps are followed to preprocess the data:
(i) Key attributed from various data sources merged into one dataset as part of data refining.
(ii) Missing values and nulls removed from the dataset: The mean of the row is used in the place of null values.
(iii) Categorical data identified and converted into integer values: Label encoder and onehot encoder used to convert string data to integer values
(iv) Avoiding dummy variable trap via the removal.
(v) Data scaling to the required range
(vi) Divide the data to test and train.
The correlation between the attributes is calculated through Linear regression.
VI. ALGORITHM APPROACH
The algorithm applied to our pre-processed data is multi linear regression. This algorithm is the best fit for our refined data. Coefficient values and multiple collinearity are derived from the algorithm.
Equation:
y = constant + c1*HDI + c2*Number of Internet Users+c3*distance from equator + c4*number of athletes +c5*population + c6*GDP
Here constant is: “1” if the country is the host country and “0” is the country in a not the host country.
VII. ACCURACY
Accuracy is calculated using the following equation:
Error % = Predicted value - Actual value
Error % -100 = accuracy
Achieved Accuracy = 53%
VIII. VALUE PREDICTION
Values from the user are providing input to the trained model. The model predicts the medal count of the nations based on the range of values selected by the users.
REFERENCES
[1]. http://bl.ocks.org
[2]. https://www.kaggle.com
[3] https://www.udemy.com/
[4]. http://www.worldbank.org/
[5]. http://www.oced.org/
[6]. http://www.courser.org/
[7]. https://conda.io/docs/download.html
[8]. https://anaconda.org/anaconda/spyder
[9]. https://stackoverflow.com/
[10]. https://www.w3schools.com/
[11]. https://bl.ocks.org/mbostock/3885304
[12]. https://bl.ocks.org/mbostock/7ea1dde508cec6d2d95306f92642bc42
[13]. https://bl.ocks.org/mbostock/4060954
[14]. https://bl.ocks.org/mbostock/3883245
[15]. https://bl.ocks.org/mbostock/3886208
