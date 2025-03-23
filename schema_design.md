# Coding Contest Platform - SQL to NoSQL Schema Conversion using MongoDB

## Schema Overview

MongoDB, being a NoSQL database, uses a document-oriented data model. Instead of using tables with rows and columns like SQL, MongoDB stores data in flexible, JSON-like documents. For this project, we identified the key entities in the SQL schema (**Users, Contests, Problems, etc.**) and restructured them as MongoDB collections.

- **Embedding** is used when entities are tightly related and frequently accessed together.  
- **References** are used for more complex relationships that need scalability.

## Collections and Data Structures

### Users Collection

```json
{
  "_id": "user_id",
  "name": "User's name",
  "email": "user@example.com",
  "phone_number": "1234567890",
  "overall_rank": 5,
  "user_created_at": "2023-03-22T12:00:00Z",
  "user_updated_at": "2023-03-22T12:00:00Z",
  "details": {
    "bio": "User bio",
    "skills": "User skills",
    "achievements": "User achievements"
  },
  "social_media_links": [
    {
      "platform_name": "LinkedIn",
      "link": "https://linkedin.com/userprofile"
    },
    {
      "platform_name": "GitHub",
      "link": "https://github.com/userprofile"
    }
  ],
  "addresses": [
    {
      "address": "User address",
      "state": "State",
      "country": "Country",
      "pincode": "123456",
      "updated_at": "2023-03-22T12:00:00Z"
    }
  ]
}
```

### Contests Collection

```json
{
  "_id": "contest_id",
  "host_id": "user_id",
  "contest_name": "Contest name",
  "start_date_time": "2023-04-01T10:00:00Z",
  "end_date_time": "2023-04-01T12:00:00Z",
  "organization_type": "Organization type",
  "organization_name": "Organization name",
  "participant_limit": 100,
  "contest_visibility": "Public",
  "contest_created_at": "2023-03-22T12:00:00Z",
  "contest_updated_at": "2023-03-22T12:00:00Z",
  "registration_deadline": "2023-03-31T12:00:00Z",
  "details": {
    "contest_banner_image": "https://example.com/banner.jpg",
    "about": "About the contest",
    "eligibility": "Eligibility criteria",
    "rules": "Contest rules"
  },
  "prizes": [
    {
      "prize_position": "First",
      "prize_description": "Description of first prize",
      "prize_amount": 500.00
    },
    {
      "prize_position": "Second",
      "prize_description": "Description of second prize",
      "prize_amount": 300.00
    }
  ],
  "problems": [
    {
      "problem_id": "problem_id",
      "name": "Problem name",
      "description": "Problem description",
      "input_format": "Input format",
      "output_format": "Output format",
      "constraints": "Problem constraints",
      "difficulty_level": "Medium",
      "test_cases": [
        {
          "input": "Test case input",
          "expected_output": "Expected output",
          "time_limit": 1,
          "memory_limit": 256
        }
      ]
    }
  ]
}
```

### Contest Registrations Collection

```json
{
  "_id": "registration_id",
  "participant_id": "user_id",
  "contest_id": "contest_id",
  "registration_date_and_time": "2023-03-22T12:00:00Z",
  "contest_submission_time": "2023-04-01T12:30:00Z",
  "total_time_taken": 7200
}
```

### Submissions Collection

```json
{
  "_id": "submission_id",
  "contest_id": "contest_id",
  "problem_id": "problem_id",
  "participant_id": "user_id",
  "submitted_at": "2023-04-01T11:30:00Z",
  "language": {
    "language_id": "language_id",
    "language": "Python"
  },
  "code": "Submitted code here",
  "score": 95.50,
  "test_case_results": [
    {
      "testcase_id": "testcase_id",
      "is_passed": true,
      "execution_time": 0.2,
      "memory_used": 256
    }
  ]
}
```

### Problems Collection

```json
{
  "_id": "problem_id",
  "host_id": "user_id",
  "name": "Problem name",
  "description": "Problem description",
  "input_format": "Input format",
  "output_format": "Output format",
  "constraints": "Problem constraints",
  "difficulty_level": "Medium",
  "test_cases": [
    {
      "testcase_id": "testcase_id",
      "input": "Test case input",
      "expected_output": "Expected output",
      "time_limit": 1,
      "memory_limit": 256
    }
  ]
}
```

## Key Points

- **Embedding**: Used for fields such as `details`, `social_media_links` in **Users**, and `problems`, `prizes` in **Contests** to avoid unnecessary queries and speed up retrieval.
- **References**: Applied in places where relationships need to remain flexible, such as between **Users and Contests** or between **Contests and Problems**, allowing for independent updates.
- **Test Cases**: Stored as embedded documents within the **Problems** collection to maintain simplicity and data consistency.

## Conclusion

This NoSQL schema for a coding contest platform is optimized for performance and flexibility using **MongoDB's document-based model**. The combination of **embedding** for frequently accessed data and **referencing** for scalability ensures an efficient schema design.
