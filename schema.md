# NoSql Schema design for the application

```json
{
  "users": {
    "_id": "ObjectId",
    "name": "string",
    "email": "string",
    "phone_number": "string (nullable)",
    "login_password": "string",
    "overall_rank": "int",
    "user_created_at": "ISODate",
    "user_updated_at": "ISODate",
    "details": {
      "bio": "text",
      "skills": ["array of strings"],
      "achievements": ["array of strings"]
    },
    "social_media_links": [
      {
        "platform_name": "string",
        "link": "string"
      }
    ],
    "addresses": {
      "updated_at": "ISODate",
      "address": "string",
      "state": "string",
      "country": "string",
      "pincode": "string"
    }
  },
  "contests": {
    "_id": "ObjectId",
    "contest_name": "string",
    "host_id": "ObjectId",
    "contest_start_date": "ISODate",
    "contest_end_date": "ISODate",
    "organisation": {
      "type": "string",
      "name": "string"
    },
    "participant_limit": "int",
    "contest_visibility": "string",
    "contest_created_at": "ISODate",
    "contest_updated_at": "ISODate",
    "registration_deadline": "ISODate",
    "details": {
      "contest_banner_image": "string",
      "contest_default_banner_image": "string",
      "about": "text",
      "eligibility": "text",
      "rules": "text",
      "others": "text"
    },
    "prizes": [
      {
        "prize_position": "int",
        "prize_description": "text",
        "prize_amount": "decimal",
        "others": "text",
        "winner": "ObjectId (nullable)"
      }
    ]
  },
  "contest_registrations": {
    "_id": "ObjectId",
    "participant_id": "ObjectId",
    "contest_id": "ObjectId",
    "registration_date_and_time": "ISODate",
    "contest_submission_time": "ISODate",
    "total_time_taken": "ISODate"
  },
  "problems": {
    "_id": "ObjectId",
    "host_id": "ObjectId",
    "title": "string",
    "description": "text",
    "input_format": "text",
    "output_format": "text",
    "constraints": "text",
    "difficulty_level": "string",
    "created_at": "ISODate",
    "updated_at": "ISODate",
    "references": "text",
    "weightage": "int",
    "sample_tests": [
      {
        "sample_input": "text",
        "sample_output": "text"
      }
    ],
    "test_cases": [
      {
        "input": "text",
        "expected_output": "text",
        "expected_output_type": "text",
        "time_limit": "decimal",
        "memory_limit": "decimal"
      }
    ]
  },
  "submissions": {
    "_id": "ObjectId",
    "contest_id": "ObjectId",
    "problem_id": "ObjectId",
    "user_id": "ObjectId",
    "submitted_at": "ISODate",
    "language": "string",
    "code": "text",
    "score": "decimal",
    "results": [
      {
        "testcase_id": "ObjectId",
        "is_passed": "boolean",
        "execution_time": "decimal",
        "memory_used": "decimal"
      }
    ]
  },
  "participant_ranking": {
    "_id": "ObjectId",
    "contest_id": "ObjectId",
    "user_id": "ObjectId",
    "rank": "int",
    "total_score": "decimal",
    "time_taken": "decimal"
  }
}
