# Image Classification (Bachelor project)



## About the project

The project's objective is to create an application to facilitate the training and evaluation of neural networks in Image Classification.

<i>The initial plan was to build this application in two phases. The first phase (my bachelor's project) meant building the required features as solid as possible, while making sure that in the future features can be added without any problems. The second phase was supposed to be a dissertation thesis in Artificial Intelligence and Computer Vision in which I would have used it to experiment with various CNN models. But in the end the plan changed, so only the first phase is completed ... at least for now :).</i>


## Key requirements

<ul>
	<li>While creating a new training or a new evaluation session, the application must allow the user to choose between different NN models.</li>
	<li>Allow the user to create data sets.</i>
	<li>Facilitate training and evaluation by allowing the continuation of an existing session.</li>
	<li>Display in a concise format meaningful informations during and after the training and evaluation sessions.</li>
	<li>Check the integrity of data set and session files.</li>
	<li>Automatically download the required files if the user wants to use Cifar 10.</i>
</ul>


## Features

<table>
    <tr>
        <th> Feature </th>
        <th> Feature description </th>
    </tr>
    <tr>
        <td> Data set creation </td>
        <td> Cifar 10 and/or user provided images. </td>
    </tr>
    <tr>
        <td> Train neural network </td>
        <td> The user can create a new training session or continue an existing one. </td>
    </tr>
    <tr>
        <td> Evaluate neural network </td>
        <td>
            <ul>
                <li> Manual testing - <i>The user selects the desired session and an image to be evaluated.</i> </li>
                <li> Automated testing - <i>The user selects the desired session and a data set.</i> </li>
                <li> Model evaluating - <i>K-fold cross-validation</i> </li>
            </ul>
        </td>
    </tr>
</table>

Due to time constraints the only CNN model currently implemented is the one provided at the time as an example in TF's documentation.


## Requirements

Project developed on Linux, not tested with newer versions (>= 2017) or on Windows.
	
*  Python 3.6.1 + Pillow + Image
*  Tensorflow 1.2


## Copyright

### Images used in the application

<table>
	<tr>
		<th> Interface </th>
		<th> The image is used in </th>
		<th> Copyright details </th>
	</tr>
	<tr>
		<td rowspan="7"> Main GUI </td>
		<td> <b>"Info"</b> button </td>
		<td> Icon made by <a href="http://www.flaticon.com/authors/madebyoliver" title="Madebyoliver">Madebyoliver</a> from <a href="http://www.flaticon.com" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a> </td>
	</tr>
	<tr>
		<td> <b>"Create data set"</b> button </td>
		<td> Icon made by <a href="http://www.flaticon.com/authors/madebyoliver" title="Madebyoliver">Madebyoliver</a> from <a href="http://www.flaticon.com" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a> </td>
	</tr>
	<tr>
		<td> <b>"Train"</b> button </td>
		<td> Icon made by <a href="http://www.flaticon.com/authors/tracy-tam" title="Tracy Tam">Tracy Tam</a> from <a href="http://www.flaticon.com" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a> </td>
	</tr>
	<tr>
		<td> <b>"Test"</b> button </td>
		<td> Icon made by <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="http://www.flaticon.com" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a> </td>
	</tr>
	<tr>
		<td> <b>"Interact"</b> button </td>
		<td> Icon made by <a href="http://www.flaticon.com/authors/kirill-kazachek" title="Kirill Kazachek">Kirill Kazachek</a> from <a href="http://www.flaticon.com" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a> </td>
	</tr>
	<tr>
		<td> <b>"Help"</b> button </td>
		<td> Icon made by <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="http://www.flaticon.com" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a> </td>
	</tr>
	<tr>
		<td> <b>"Exit"</b> button </td>
		<td> Icon made by <a href="http://www.flaticon.com/authors/madebyoliver" title="Madebyoliver">Madebyoliver</a> from <a href="http://www.flaticon.com" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a> </td>
	</tr>
	<tr>
		<td rowspan="2"> Train session GUI </td>
		<td> <b>"New training session"</b> button </td>
		<td> Icon made by <a href="http://www.flaticon.com/authors/madebyoliver" title="Madebyoliver">Madebyoliver</a> from <a href="http://www.flaticon.com" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a> </td>
	</tr>
	<tr>
		<td> <b>"Existent training session"</b> button </td>
		<td> Icon made by <a href="http://www.flaticon.com/authors/madebyoliver" title="Madebyoliver">Madebyoliver</a> from <a href="http://www.flaticon.com" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a> </td>
	</tr>
	<tr>
		<td rowspan="2"> Test session GUI </td>
		<td> <b>"Automated test session"</b> button </td>
		<td> Icon made by <a href="http://www.flaticon.com/authors/gregor-cresnar" title="Gregor Cresnar">Gregor Cresnar</a> from <a href="http://www.flaticon.com" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a> </td>
	</tr>
	<tr>
		<td> <b>"Manual test session"</b> button </td>
		<td> Icon made by <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="http://www.flaticon.com" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a> </td>
	</tr>
</table>
