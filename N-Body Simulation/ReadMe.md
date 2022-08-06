<h1>N-body Simulation using Newtonian Physics</h1>

<h3> Definition:</h3>
As Newton declared the Body of Mass M Experiencing a Force F,
accelerates with an acceleration of F/M we use the same principle develop the n-body simulation

<b><span class="md-formula"><span class="anchor" id="ref-15559"></span></span><em>F</em><sub>g</sub>=G<em>M</em><sub>1</sub><em>M</em><sub>2</sub>/<em>r</em><sup>2</sup></b>

Where <b> G</b> is the Gravitational Constant which equals to 

<b><p> <span class="md-formula"> 0.6743 × 10<sup>−11</sup> m<sup>3</sup> s<sup>−2</sup> kg<sup>−1</sup></span></p></b>
M<sub>1</sub> and M<sub>2</sub> are the masses of the bodies and 
r<sup>2</sup> is the square of distances between the bodies

For the simplicity of our simulation we will use a moderately high value of 0.01

Then to calculate the radius of the object, we simplify the radius of a sphere calculated as 
<p> <b> r = 3√(mass/density)</b></p>

To calculate the distance between the objects, we use Euclidean distance.

Finally, for the graphical representation we use Tkinter, with a fixed refresh rate of the canvas.



