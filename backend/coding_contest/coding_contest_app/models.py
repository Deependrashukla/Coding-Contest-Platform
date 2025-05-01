from mongoengine import ( # type: ignore
    Document, EmbeddedDocument, StringField, EmailField, DateTimeField, 
    IntField, FloatField, ListField, EmbeddedDocumentField, BooleanField
)
import datetime

# ======= Embedded Documents =======

class UserDetails(EmbeddedDocument):
    bio = StringField()
    skills = StringField()
    achievements = StringField()

class SocialMediaLink(EmbeddedDocument):
    platform_name = StringField()
    link = StringField()

class Address(EmbeddedDocument):
    address = StringField()
    state = StringField()
    country = StringField()
    pincode = StringField()
    updated_at = DateTimeField(default=datetime.datetime.utcnow)

class Prize(EmbeddedDocument):
    prize_position = StringField()
    prize_description = StringField()
    prize_amount = FloatField()

class TestCase(EmbeddedDocument):
    input = StringField()
    expected_output = StringField()
    time_limit = IntField()
    memory_limit = IntField()
    testcase_id = StringField()  # for Submissions and Problems both

class Problem(EmbeddedDocument):
    problem_id = StringField()
    name = StringField()
    description = StringField()
    input_format = StringField()
    output_format = StringField()
    constraints = StringField()
    difficulty_level = StringField()
    test_cases = ListField(EmbeddedDocumentField(TestCase))

class Language(EmbeddedDocument):
    language_id = StringField()
    language = StringField()

class TestCaseResult(EmbeddedDocument):
    testcase_id = StringField()
    is_passed = BooleanField()
    execution_time = FloatField()
    memory_used = IntField()

# ======= Main Collections =======

class User(Document):
    _id = StringField(primary_key=True)
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    phone_number = StringField()
    overall_rank = IntField()
    user_created_at = DateTimeField(default=datetime.datetime.utcnow)
    user_updated_at = DateTimeField(default=datetime.datetime.utcnow)
    details = EmbeddedDocumentField(UserDetails)
    social_media_links = ListField(EmbeddedDocumentField(SocialMediaLink))
    addresses = ListField(EmbeddedDocumentField(Address))

    meta = {'collection': 'users'}

class Contest(Document):
    _id = StringField(primary_key=True)
    host_id = StringField(required=True)
    contest_name = StringField(required=True)
    start_date_time = DateTimeField()
    end_date_time = DateTimeField()
    organization_type = StringField()
    organization_name = StringField()
    participant_limit = IntField()
    contest_visibility = StringField(choices=["Public", "Private"])
    contest_created_at = DateTimeField(default=datetime.datetime.utcnow)
    contest_updated_at = DateTimeField(default=datetime.datetime.utcnow)
    registration_deadline = DateTimeField()

    # Embedded fields
    details = EmbeddedDocumentField(UserDetails)
    prizes = ListField(EmbeddedDocumentField(Prize))
    problems = ListField(EmbeddedDocumentField(Problem))

    meta = {'collection': 'contests'}

class ContestRegistration(Document):
    _id = StringField(primary_key=True)
    participant_id = StringField(required=True)
    contest_id = StringField(required=True)
    registration_date_and_time = DateTimeField(default=datetime.datetime.utcnow)
    contest_submission_time = DateTimeField()
    total_time_taken = IntField()

    meta = {'collection': 'contest_registrations'}

class Submission(Document):
    _id = StringField(primary_key=True)
    contest_id = StringField(required=True)
    problem_id = StringField(required=True)
    participant_id = StringField(required=True)
    submitted_at = DateTimeField(default=datetime.datetime.utcnow)
    language = EmbeddedDocumentField(Language)
    code = StringField()
    score = FloatField()
    test_case_results = ListField(EmbeddedDocumentField(TestCaseResult))

    meta = {'collection': 'submissions'}

class ProblemBank(Document):  # Centralized problem store
    _id = StringField(primary_key=True)
    host_id = StringField(required=True)
    name = StringField()
    description = StringField()
    input_format = StringField()
    output_format = StringField()
    constraints = StringField()
    difficulty_level = StringField()
    test_cases = ListField(EmbeddedDocumentField(TestCase))

    meta = {'collection': 'problems'}
