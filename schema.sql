PRAGMA foreign_keys = ON; --enables the enforcement of foreign key support

-- Organizations
CREATE TABLE organizations (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL
);

-- Teams
CREATE TABLE teams (
    id TEXT PRIMARY KEY,
    organization_id TEXT NOT NULL,
    name TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (organization_id) REFERENCES organizations(id)
);

-- Users
CREATE TABLE users (
    id TEXT PRIMARY KEY,
    organization_id TEXT NOT NULL,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    role TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (organization_id) REFERENCES organizations(id)
);

-- Team memberships
CREATE TABLE team_memberships (
    team_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    PRIMARY KEY (team_id, user_id),
    FOREIGN KEY (team_id) REFERENCES teams(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Projects
CREATE TABLE projects (
    id TEXT PRIMARY KEY,
    team_id TEXT NOT NULL,
    name TEXT NOT NULL,
    project_type TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

-- Sections
CREATE TABLE sections (
    id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    name TEXT NOT NULL,
    position INTEGER NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects(id)
);

-- Tasks
CREATE TABLE tasks (
    id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    section_id TEXT NOT NULL,
    assignee_id TEXT,
    parent_task_id TEXT,
    name TEXT NOT NULL,
    description TEXT,
    due_date DATE,
    completed BOOLEAN NOT NULL DEFAULT 0,
    created_at TIMESTAMP NOT NULL,
    completed_at TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(id),
    FOREIGN KEY (section_id) REFERENCES sections(id),
    FOREIGN KEY (assignee_id) REFERENCES users(id),
    FOREIGN KEY (parent_task_id) REFERENCES tasks(id)
);

-- Comments
CREATE TABLE comments (
    id TEXT PRIMARY KEY,
    task_id TEXT NOT NULL,
    author_id TEXT NOT NULL,
    body TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (task_id) REFERENCES tasks(id),
    FOREIGN KEY (author_id) REFERENCES users(id)
);

-- Custom Field Definitions
CREATE TABLE custom_field_definitions (
    id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    name TEXT NOT NULL,
    field_type TEXT NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects(id)
);

-- Custom Field Values
CREATE TABLE custom_field_values (
    task_id TEXT NOT NULL,
    field_id TEXT NOT NULL,
    value TEXT,
    PRIMARY KEY (task_id, field_id),
    FOREIGN KEY (task_id) REFERENCES tasks(id),
    FOREIGN KEY (field_id) REFERENCES custom_field_definitions(id)
);

-- Tags
CREATE TABLE tags (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

-- Task Tags
CREATE TABLE task_tags (
    task_id TEXT NOT NULL,
    tag_id TEXT NOT NULL,
    PRIMARY KEY (task_id, tag_id),
    FOREIGN KEY (task_id) REFERENCES tasks(id),
    FOREIGN KEY (tag_id) REFERENCES tags(id)
);

-- Attachments
CREATE TABLE attachments (
    id TEXT PRIMARY KEY,
    task_id TEXT NOT NULL,
    uploaded_by TEXT NOT NULL,
    file_name TEXT NOT NULL,
    file_url TEXT,
    file_type TEXT,
    file_size INTEGER,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (task_id) REFERENCES tasks(id),
    FOREIGN KEY (uploaded_by) REFERENCES users(id)
);
