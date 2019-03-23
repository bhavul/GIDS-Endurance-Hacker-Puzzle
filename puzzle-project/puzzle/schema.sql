create table if not exists bhailog (
    name char(100) not null,
    email char(100) not null,
    phone CHAR(15) not null,
    sessionhash text,
    verifycode char(10) not null,
    progress integer,
    createdatetime DATE DEFAULT (DATETIME('NOW')),
    updatedatetime DATE DEFAULT (DATETIME('NOW')),
    PRIMARY KEY (email),
    UNIQUE (phone),
    UNIQUE (sessionhash)
);



create table if not exists khazana (
    sessionhash char(100) not null,
    time char(15) not null,
    randomstring char(11) not null,
    PRIMARY KEY (sessionhash)
);

-- here
CREATE TRIGGER if not exists update_bhailog_updatetime  AFTER update ON bhailog
begin
    update bhailog set updatedatetime = DATETIME('NOW') where email = old.email;
end;

-- here
create table if not exists events (
    sessionhash char(100) not null,
    description text,
    createdatetime DATE DEFAULT (DATETIME('NOW'))
);

create table if not exists finalsubmission (
    sessionhash char(100) not null,
    answer char(255) not null,
    linktocode text,
    PRIMARY KEY (sessionhash)
);

create table if not exists trials(
    sessionhash char(100) not null,
    progress integer,
    count integer,
    updatedatetime DATE DEFAULT (DATETIME('NOW')),
    PRIMARY KEY (sessionhash,progress)
);


CREATE TRIGGER if not exists update_trials_updatetime  AFTER update ON trials
begin
    update trials set updatedatetime = DATETIME('NOW') where sessionhash = old.sessionhash;
end;


