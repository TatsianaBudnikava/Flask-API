from flask import Blueprint, request, jsonify, abort
from .models import db, Employee, Skill

bp = Blueprint('api', __name__)

# Create Employee
@bp.route("/employees", methods=["POST"])
def create_employee():
    data = request.json
    if not data or not data.get("name") or not data.get("surname"):
        return jsonify({"error": "Invalid input"}), 400
    emp = Employee(name=data["name"], surname=data["surname"])
    db.session.add(emp)
    db.session.commit()
    return jsonify({"id": emp.id}), 201

# Update Employee
@bp.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    emp = db.session.get(Employee, employee_id)
    if not emp:
        abort(404)
    data = request.json
    emp.name = data.get("name", emp.name)
    emp.surname = data.get("surname", emp.surname)
    db.session.commit()
    return jsonify({"message": "Employee updated"})

# Delete Employee
@bp.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    emp = db.session.get(Employee, employee_id)
    if not emp:
        abort(404)
    db.session.delete(emp)
    db.session.commit()
    return jsonify({"message": "Employee deleted"}), 200

# Get all Employees
@bp.route("/employees", methods=["GET"])
def get_employees():
    employees = Employee.query.all()
    result = []
    for emp in employees:
        result.append({
            "id": emp.id,
            "name": emp.name,
            "surname": emp.surname,
            "skills": [s.name for s in emp.skills]
        })
    return jsonify(result)

# Search Employees
@bp.route("/employees/search", methods=["GET"])
def search_employees():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400
    employees = Employee.query.filter(
        (Employee.name.ilike(f"%{query}%")) |
        (Employee.surname.ilike(f"%{query}%")) |
        (Employee.skills.any(Skill.name.ilike(f"%{query}%")))
    ).all()
    result = []
    for emp in employees:
        result.append({
            "id": emp.id,
            "name": emp.name,
            "surname": emp.surname
        })
    return jsonify(result)

# Create Skill
@bp.route("/skills", methods=["POST"])
def create_skill():
    data = request.json
    if not data or not data.get("name"):
        return jsonify({"error": "Invalid input"}), 400
    skill = Skill(name=data["name"], employee_id=data.get("employee_id"))
    db.session.add(skill)
    db.session.commit()
    return jsonify({"id": skill.id, "name": skill.name}), 201

# Update Skill
@bp.route("/skills/<int:skill_id>", methods=["PUT"])
def update_skill(skill_id):
    skill = db.session.get(Skill, skill_id)
    if not skill:
        abort(404)
    data = request.json
    skill.name = data.get("name", skill.name)
    skill.employee_id = data.get("employee_id", skill.employee_id)
    db.session.commit()
    return jsonify({"id": skill.id, "name": skill.name})

# Delete Skill
@bp.route("/skills/<int:skill_id>", methods=["DELETE"])
def delete_skill(skill_id):
    skill = db.session.get(Skill, skill_id)
    if not skill:
        abort(404)
    db.session.delete(skill)
    db.session.commit()
    return '', 204

# Get all Skills
@bp.route("/skills", methods=["GET"])
def get_skills():
    skills = Skill.query.all()
    result = []
    for s in skills:
        result.append({
            "id": s.id,
            "name": s.name,
            "employee_id": s.employee_id
        })
    return jsonify(result)

# Get Skill by id
@bp.route("/skills/<int:skill_id>", methods=["GET"])
def get_skill(skill_id):
    skill = db.session.get(Skill, skill_id)
    if not skill:
        abort(404)
    return jsonify({
        "id": skill.id,
        "name": skill.name,
        "employee_id": skill.employee_id
    })
