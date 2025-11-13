from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.project import Project
from app.schemas.project import  ProjectCreate, ProjectOut
from app.database import get_db
router = APIRouter(prefix="/projects", tags=["projects"])

# CREATE

@router.post("/", response_model=ProjectOut)
def create_project(data: ProjectCreate, db: Session = Depends(get_db)):
    new_project = Project(**data.dict( ))
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

# READ ALL

@router.get("/", response_model=list[ProjectOut])
def get_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()

# READ ONE

@router.get("/{project_id}", response_model=ProjectOut)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

# UPDATE

@router.put("/{project_id}", response_model=ProjectOut)
def update_project(project_id: int, data: ProjectCreate, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    for key, value in data.dict().items():
        setattr(project, key, value)
    db.commit()
    db.refresh(project)
    return project

# DELETE

@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(project)
    db.commit()
    return {"message": "Project deleted successfully"}

