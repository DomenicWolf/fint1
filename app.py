from flask import Flask,request,render_template,redirect,flash,session
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db,db,Pet
from forms import addPetForm
app = Flask(__name__)

app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SECRET_KEY'] = 'asdasd'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def show_home():
    pets = Pet.query.all()
    return render_template('home.html',pets = pets)

@app.route('/add',methods=['GET','POST'])
def show_add_form():
    form = addPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        
        age = form.age.data
        note = form.notes.data
        avail = form.available.data
        new = Pet(name=name,species=species,age=age,notes=note,available=avail)
        if form.photo_url.data:
            photo = form.photo_url.data
            new.photo_url = photo
        db.session.add(new)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('pet_form.html',form=form)
@app.route('/<int:pet_id>',methods=['GET','POST'])
def show_details(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = addPetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.name.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        if form.photo_url.data:
            photo = form.photo_url.data
            pet.photo_url = photo
        db.session.commit()
        flash('Edited animal posting')
        return redirect('/<int:pet_id>')
    return render_template('pet_detail.html',pet=pet,form=form)

