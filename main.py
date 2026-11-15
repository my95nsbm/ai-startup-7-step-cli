from dataclasses import dataclass, field
from typing import List

STEPS = [
    ('Validate', 'Interview 5 target users and map painful workflows.'),
    ('BP', 'Write a one-page problem, solution, wedge, and model.'),
    ('Policy', 'List data, privacy, model, and compliance risks.'),
    ('Pitch', 'Craft a 30-second demo story and 5-slide deck.'),
    ('Growth', 'Pick one channel and define an activation metric.'),
    ('Pricing', 'Test 3 price points with 10 prospects.'),
    ('Register', 'Choose entity, domain, bank, and founder admin.'),
]

@dataclass
class StartupPlan:
    idea: str
    steps: List[str] = field(default_factory=list)

def build_plan(idea: str) -> StartupPlan:
    plan = StartupPlan(idea=idea.strip())
    for i, (name, action) in enumerate(STEPS, 1):
        plan.steps.append(f'{i}. {name}: {action}')
    return plan

def score_idea() -> int:
    questions = [
        'Do users already pay for a workaround? (y/n) ',
        'Can you demo value in under 10 minutes? (y/n) ',
        'Is the first wedge narrow enough? (y/n) ',
        'Do you have 10 reachable prospects? (y/n) ',
        'Can you ship an MVP in 2 weeks? (y/n) ',
    ]
    return sum(input(q).strip().lower().startswith('y') for q in questions)

def main() -> None:
    print('AI Startup 7-Step Planner')
    idea = input('Describe your AI startup idea: ')
    plan = build_plan(idea)
    print()
    print('Idea:', plan.idea)
    print()
    print(chr(10).join(plan.steps))
    print()
    print('Quick validation score (0-5):', score_idea())
    print('Next action: talk to 5 users before writing more code.')

if __name__ == '__main__':
    main()
