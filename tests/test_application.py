import unittest 
from flask_testing import TestCase
from flask import url_for
from application import app, db
from application.models import Exercise, Goal

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLAlCHEMY_DATABASE_URI= "sqlite:///dull.db")
        return app

    def setUp(self):
        db.create_all()
        #sample data
        sample1 = Exercise(name="run",done="5km",date="04-02-2021")
        sample2 = Goal(goal_name="run5km", goal_setdate="04-02-2021", goal_finishdate="30-09-2021")
        #save Exercise data to database
        db.session.add(sample1)
        db.session.add(sample2)
        db.session.commit()


    def tearDown(self):
        db.session.remove()
        db.drop_all()

#test acccess to home and goal 
class TestAccess(TestBase):
    def test_access_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    def test_access_goal(self):
        response = self.client.get(url_for('editgoal'))
        self.assertEqual(response.status_code, 200)

#test data add data for exercise and goal
class TestAdd(TestBase):
    def test_data_add_exercise(self):
        response = self.client.post(
            url_for('home'),
            data = dict(name="gym", done="back 25kg", date="04-02-21"))
        self.assertIn(b'gym', response.data)
    def test_data_add_goal(self):
        response = self.client.post(
            url_for('editgoal'),
            data = dict(goal_name="run5km", goal_setdata="2021", goal_finishdate="2022"))
        self.assertIn(b'run5km', response.data)


#test data update data for exercise and goal
class TestUpdate(TestBase):
    def test_data_update_exercise(self):
        response = self.client.post(
            url_for('update'),
            data = dict(oldname="run", newname="run triple"),
            follow_redirects= True
            )
        self.assertEqual(response.status_code, 200)
    def test_data_update_goal(self):
        response = self.client.post(
            url_for('updategoal'),
            data = dict(oldid=1, newname="changegoal"),
            follow_redirects = True
            )
        self.assertEqual(response.status_code, 200)

class TestDelete(TestBase):
    def test_data_delete_exercise(self):
        response = self.client.post(
            url_for('delete'),
            data = dict(name="run"),
            follow_redirects= True
            )
        self.assertEqual(response.status_code, 200)
    def test_data_delete_goal(self):
        response = self.client.post(
            url_for('deletegoal'),
            data = dict(id=1),
            follow_redirects = True
            )
        self.assertEqual(response.status_code, 200)