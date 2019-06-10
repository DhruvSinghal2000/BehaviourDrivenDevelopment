from  behave import*
from Operations import *
import math
use_step_matcher("re")

@given('Calculator template to perform trigo functions')
def step_impl(context):
    pass


@when('User Inputs parameter to cos function in radians (?P<numbers>(?:\d*\.?\d*))')
def step_impl(context , numbers):
    context.response = numbers
    #pass


@then('output its cosine value (?P<numbers>(?:\d*\.?\d*))')
def step_impl(context, numbers):
    assert Calculator.cos(context.response) == float(numbers)


