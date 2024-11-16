def variables_dict_builder() -> dict:
    # VARIABLES USED IN MODEL
    outcomes_dict = {
                    'nrshom':'Nursing home stay in the previous 2 years', 
                    'nhmliv':'Live in Nursing home at Interview', # PRIMARY OUTCOME
    }

    demographics_dict = {
                        # SECTION A: Demographics and Identifiers in randhrs1992_2020v2.pdf
                        'hhidpn': 'HHold ID + Person Number',
                        'byear': 'Birth Year', # r_byear for individual, s_byear for spouse
                        'bmonth': 'Birth Month',
                        'dyear': 'Death Year',
                        'dmonth': 'Death Month',
                        'gender':'',
                        'racem':'Race - Masked',
                        'hispan':'',
                        'mstat':'Marital Status', # 8 levels
                        'relig':'Religion', # 5 levels
                        'vetrn':'Veteran Status', # Binary
                        'cenreg':'Census Region', # 4 levels e.g. South
                        'cendiv':'Census Division', # 8 levels e.g. Mid-Atlantic
                        'urbrur':'Urban-Suburban-Rural', # 1=Urban, 2=Suburban, 3=Rural   
                        'edyrs':'Education in years',
                        'edegrm':'Highest degree - Masked',
                        'educ':'Education level', # 5 levels e.g. Some College, GED, ...
                        'meduc':'Mother\'s years education',
                        'feduc':'Father\'s years education',
                        'momage':'Mother age current/at death',
                        'dadage':'Father age current/at death',
                        # SECTION I: Household structure
                        'hhres':'number of people in household',
                        'child':'number of living children',
                        'livsib':'number of living siblings',
                        # SECTION J: Retirement Plans/Expectations
                        # --- includes measures of self reported retirement or continued work after various ages
                        # --- includes measures of self reported expectations of life expectancy
                        # --- includes measures of self reported inheritance and bequest expectations
    }

    income_dict = {
                    # SECTION D: Financial and Housing Wealth
                    'atotn':'Total Non-housing Wealth',
                    # SECTION E:
                    'itot':'Total household income (Respondent & spouse)',
                    'inpov':'Whether in Poverty',
    }

    frailty_dict = {
    # '''
    # Variables included in paper Table A-5
    # Note: the suffix 'a' represents "Any", transforming these variables from their numeric scale of severity to binary
    # '''
                    # ADLs
                    'batha':'Any difficulty bathing',
                    'dressa':'Any difficulty dressing',
                    'eata':'Any difficulty eating',
                    'beda':'Any difficulty getting in/out of bed',
                    'toilta':'Any difficulty using toilet',
                    'walkra':'Any difficulty walking across a room',
                    'walk1a':'Any difficulty walking 1 block',
                    'walksa':'Any difficulty walking several blocks',
                    # IADLs
                    'shopa':'Any difficulty shopping for groceries',
                    'phonea':'Any difficulty making a phone call',
                    'moneya':'Any difficulty managing money',
                    'mealsa':'Any difficulty preparing a meal',
                    'medsa':'Any difficulty ',
                    'mapa':'Any difficulty ',
                    # Other functional limitations
                    'clim1a':'Any difficulty climbing 1 flight of stairs',
                    'climsa':'Any difficulty climbing several flights of stairs',
                    'chaira':'Any difficulty getting up from a chair',
                    'stoopa':'Any difficulty kneeling, stooping, crouching',
                    'lifta':'Any difficulty lifting over 10 lbs',
                    'armsa':'Any difficulty lifting arms above the shoulders',
                    'dimea':'Any difficulty picking up a dime from a table',
                    'pusha':'Any difficulty pushing or pulling large objects',
                    'sita':'Any difficulty sitting for over 2 hours',
                    # Diagnoses
                    'arthre':'Arthritis or rheumatisms binary',
                    'cancre':'Cancer or a malignant tumor of any kind except skin cancer binary',
                    'diabe':'Diabetes or high blood sugar binary',
                    'hearte':'Heart attack, coronary heart disease, angina, congestive heart failure, or other heart problem binary',
                    'hibpe':'High blood pressure binary',
                    'lunge':'Chronic lung disease except asthma such as chronic bronchitis or emphysema binary',
                    'psyche':'Emotional, nervous, or psychiatric problems binary',
                    'stroke':'Stroke',
                    # Healthcare utilization
                    'hosp':'Hospital stay in the previous 2 years',
                    'nrshom':'Nursing home stay in the previous 2 years', # Note that this may be a conflicting measure or the outcome itself
                    # Addictive Diseases
                    'bmi': 'Self-reported BMI',
                    'pmbmi': 'Physically measured BMI',
                    'smokev':'Ever smoked',
    }

    return {**outcomes_dict, **demographics_dict, **income_dict, **frailty_dict}
