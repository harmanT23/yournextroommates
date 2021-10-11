import React from 'react'
import Typography from '@material-ui/core/Typography'
import Slider from '@material-ui/core/Slider'
import { useHistory } from 'react-router-dom'

function valuetext(value) {
  return `${value}$`
}

const formField = {
  province__iexact: '',                
  city__iexact: '',                   
  rent_per_month__lte: '',             
  rent_per_month__gte: '',           
  extra_expenses_per_month__lte: '',    
  extra_expenses_per_month__gte: '',    
  earliest_move_in_date__iexact: '',    
  length_of_lease__lte: '',            
  length_of_lease__gte: '',        
  room_type: '',                        
  is_furnished: '',                 
  is_laundry_ensuite: '',             
  is_air_conditioned: '',             
  poster__university__iexact: '',       
  poster__university_major__iexact: '', 
  poster__profession__iexact: '',      
  rent_per_month_sort: '',             
  length_of_lease_sort: '',             
  earliest_move_in_date_sort: '',
}

const Form = React.forwardRef(() => {
  // const classes = useStyles();
  const history = useHistory()

  // Slider states
  const [RentSlider, setRentSlider] = React.useState([600, 1250])
  const [ExtraExpensesSlider, setExtraExpensesSlider] = React.useState([20, 60])
  const [LengthLeaseSlider, setLengthLeaseSlider] = React.useState([4, 12])
  
  // Rent Sliders
  const handleRentSlider = (event, newValue) => {
    setRentSlider(newValue)
  }
  const handleMinRent = (e) => {
    setRentSlider([e.target.value, RentSlider[1]])
  }
  const handleMaxRent = (e) => {
    setRentSlider([RentSlider[0], e.target.value])
  }

  // Expenses Sliders
  const handleExtraExpensesSlider = (event, newValue) => {
    setExtraExpensesSlider(newValue)
  }
  const handleMinExpenses = (e) => {
    setExtraExpensesSlider([e.target.value, ExtraExpensesSlider[1]])
  }
  const handleMaxExpenses = (e) => {
    setExtraExpensesSlider([ExtraExpensesSlider[0], e.target.value])
  }

  // length lease slider function
  const handleLengthLeaseSlider = (event, newValue) => {
    setLengthLeaseSlider(newValue)
  }
  const handleMaxlease = (e) => {
    setLengthLeaseSlider([LengthLeaseSlider[0], e.target.value])
  }
  const handleMinlease = (e) => {
    setLengthLeaseSlider([e.target.value, LengthLeaseSlider[1]])
  }

  // input field values and select function
  const [inputValues, setInputValues] = React.useState(formField)
  const handleInputSelect = (event) => {
    setInputValues({ ...inputValues, [event.target.name]: event.target.value })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()

    let {
      province__iexact,             
      city__iexact,                 
      earliest_move_in_date__iexact,  
      room_type,                     
      is_furnished,                 
      is_laundry_ensuite,        
      is_air_conditioned,            
      poster__university__iexact,    
      poster__university_major__iexact,
      poster__profession__iexact,     
    } = inputValues;

    /* Todo
     * - rent_per_month_sort,            
     * - length_of_lease_sort,            
     * - earliest_move_in_date_sort,
     */

    var minRent = 600;
    var maxRent = 1250;
    var minExpense = 20;
    var maxExpense = 60;
    var minLease = 4;
    var maxLease = 12;

    if (RentSlider[0] === 600) {
      minRent = '';
    } else {
      minRent = RentSlider[0];
    }

    if (RentSlider[1] === 1250) {
      maxRent = '';
    } else {
      maxRent = RentSlider[1];
    }

    if (ExtraExpensesSlider[0] === 20) {
      minExpense = '';
    } else {
      minExpense = ExtraExpensesSlider[0];
    }

    if (ExtraExpensesSlider[1] === 60) {
      maxExpense = '';
    } else {
      maxExpense = ExtraExpensesSlider[1];
    }

    if (LengthLeaseSlider[0] === 4) {
      minLease = '';
    } else {
      minLease = LengthLeaseSlider[0];
    }

    if (LengthLeaseSlider[1] === 12) {
      maxLease = '';
    } else {
      maxLease = LengthLeaseSlider[1];
    }

    let url = new URLSearchParams([
      ['province__iexact', province__iexact],
      ['city__iexact', city__iexact],
      ['rent_per_month__lte', maxRent],
      ['rent_per_month__gte', minRent],
      ['extra_expenses_per_month__lte', maxExpense],
      ['extra_expenses_per_month__gte', minExpense],
      ['earliest_move_in_date__iexact', earliest_move_in_date__iexact],
      ['length_of_lease__lte', maxLease],
      ['length_of_lease__gte', minLease],
      ['room_type', room_type],
      ['is_furnished', is_furnished],
      ['is_laundry_ensuite', is_laundry_ensuite],
      ['is_air_conditioned', is_air_conditioned],
      ['poster__university__iexact', poster__university__iexact],
      ['poster__university_major__iexact', poster__university_major__iexact],
      ['poster__profession__iexact', poster__profession__iexact],
    ]); 

    setInputValues(formField);

    var query = url.toString();

    history.push({
      pathname: 'search',
      search: '?' + query,
    });
    window.location.reload();    
  }

  return (
    <div 
      className='form_container'
    >
      <div 
        className='form_md'
      >
        <div 
          className='head'
        >
          <h2>Search Filters</h2>
        </div>
        <form
          onSubmit={handleSubmit}
          className='filter_form'
        >
          <div className='inputs'>
            <label htmlFor='province'>
              Province
              <br />
              <input
                type='text'
                name='province__iexact'
                id='province__iexact'
                placeholder='Province'
                required
                onChange={handleInputSelect}
              />
            </label>
          </div>
          <div className='inputs'>
            <label htmlFor='city'>
              City
              <br />
              <input
                type='text'
                name='city__iexact'
                id='city__iexact'
                placeholder='City'
                required
                onChange={handleInputSelect}
              />
            </label>
          </div>
          <div className='inputs'>
            <Typography id='range-slider' gutterBottom>
              Rent per Month
            </Typography>
            <div className='range_boxes'>
              <label htmlFor=''>
                <input
                  type='text'
                  value={`${RentSlider[0]}`}
                  onChange={handleMinRent}
                />
              </label>
              <label htmlFor=''>
                <input
                  type='text'
                  value={`${RentSlider[1]}`}
                  onChange={handleMaxRent}
                />
              </label>
            </div>
            <Slider
              value={RentSlider}
              onChange={handleRentSlider}
              name='rent_per_month_range'
              valueLabelDisplay='auto'
              aria-labelledby='range-slider'
              getAriaValueText={valuetext}
              min={0}
              max={5000}
            />
          </div>

          <div className='inputs'>
            <Typography id='range-slider' gutterBottom>
              Additional Expenses per Month
            </Typography>
            <div className='range_boxes'>
              <label htmlFor=''>
                <input
                  type='text'
                  value={`${ExtraExpensesSlider[0]}`}
                  onChange={handleMinExpenses}
                />
              </label>
              <label htmlFor=''>
                <input
                  type='text'
                  value={`${ExtraExpensesSlider[1]}`}
                  onChange={handleMaxExpenses}
                />
              </label>
            </div>
            <Slider
              value={ExtraExpensesSlider}
              onChange={handleExtraExpensesSlider}
              name='extra_expenses_per_month'
              valueLabelDisplay='auto'
              aria-labelledby='range-slider'
              getAriaValueText={valuetext}
              min={0}
              max={500}
            />
          </div>
          <div className='inputs'>
            <label htmlFor='extra_expenses_per_month'>
              Earliest Move-in Date
              <br />
              <input
                type='date'
                name='earliest_move_in_date__iexact'
                id='earliest_move_in_date__iexact'
                onChange={handleInputSelect}
              />
            </label>
          </div>

          <div className='inputs'>
            <Typography id='range-slider' gutterBottom>
              Length of Lease
            </Typography>
            <div className='range_boxes'>
              <label htmlFor=''>
                <input
                  type='text'
                  value={`${LengthLeaseSlider[0]}`}
                  onChange={handleMinlease}
                />
              </label>
              <label htmlFor=''>
                <input
                  type='text'
                  value={`${LengthLeaseSlider[1]}`}
                  onChange={handleMaxlease}
                />
              </label>
            </div>
            <Slider
              value={LengthLeaseSlider}
              onChange={handleLengthLeaseSlider}
              valueLabelDisplay='auto'
              aria-labelledby='range-slider'
              getAriaValueText={valuetext}
              min={0}
              max={12}
            />
          </div>
          <div className='inputs'>
            <label htmlFor='room_type'>
              Room type
              <br />
              <select
                name='room_type'
                id='room_type'
                onChange={handleInputSelect}
              >
                <option value='unknow'>Choose a room type</option>
                <option value='Bedroom'>Bedroom</option>
                <option value='Shared Bedroom'>Shared Bedroom</option>
                <option value='Den'>Den</option>
                <option value='Living Room'>Living Room</option>
                <option value='Shared Living Room'>Shared Living Room</option>
                <option value='Sunroom'>Sunroom</option>
                <option value='Closet'>Closet</option>
              </select>
            </label>
          </div>
          <div className='inputs'>
            <label htmlFor='is_furnished'>
              <input
                className='inp_check'
                type='checkbox'
                name='is_furnished'
                id='is_furnished'
                value='true'
                onChange={handleInputSelect}
              />
              Furnished
            </label>
          </div>
          <div className='inputs'>
            <label htmlFor='is_air_conditioned'>
              <input
                className='inp_check'
                type='checkbox'
                name='is_air_conditioned'
                id='is_air_conditioned'
                value='true'
                onChange={handleInputSelect}
              />
              Air Conditioned
            </label>
          </div>
          <div className='inputs'>
            <label htmlFor='is_laundry_ensuite'>
              <input
                className='inp_check'
                type='checkbox'
                name='is_laundry_ensuite'
                id='is_laundry_ensuite'
                value='true'
                onChange={handleInputSelect}
              />
              Ensuite Laundry
            </label>
          </div>
          <div className='inputs'>
            <label htmlFor='poster_uni'>
              Roommate's University
              <br />
              <input
                type='text'
                name='poster__university__iexact'
                id='poster__university__iexact'
                onChange={handleInputSelect}
              />
            </label>
          </div>
          <div className='inputs'>
            <label htmlFor='poster_uni_major'>
              Roommates's University Major
              <br />
              <input
                type='text'
                name='poster__university_major__iexact'
                id='poster__university_major__iexact'
                onChange={handleInputSelect}
              />
            </label>
          </div>
          <div className='inputs'>
            <label htmlFor='poster_profession'>
              Roommate's Profession
              <br />
              <input
                type='text'
                name='poster__profession__iexact'
                id='poster__profession__iexact'
                onChange={handleInputSelect}
              />
            </label>
          </div>
          <div className='inputs'>
            <label htmlFor='rent_per_month_sort'>
              Rent per Month Ascending/Descending
              <br />
              <select
                name='rent_per_month_sort'
                id='rent_per_month_sort'
                onChange={handleInputSelect}
              >
                <option value=''>Choose Ascending/Descending</option>
                <option value=''>Ascending &#8593; </option>
                <option value='-'>Descending &#8595; </option>
              </select>
            </label>
          </div>
          <div className='inputs'>
            <label htmlFor='length_of_lease_sort'>
              Length of Lease Ascending/Descending
              <br />
              <select
                name='length_of_lease_sort'
                id='length_of_lease_sort'
                onChange={handleInputSelect}
              >
                <option value=''>Choose Ascending/Descending</option>
                <option value=''>Ascending &#8593; </option>
                <option value='-'>Descending &#8595; </option>
              </select>
            </label>
          </div>
          <div className='inputs'>
            <label htmlFor='earliest_move_in_date_sort'>
              Earliest Move-in Date Ascending/Descending
              <br />
              <select
                name='earliest_move_in_date_sort'
                id='earliest_move_in_date_sort'
                onChange={handleInputSelect}
              >
                <option value=''>Choose Ascending/Descending</option>
                <option value=''>Ascending &#8593; </option>
                <option value='-'>Descending &#8595; </option>
              </select>
            </label>
          </div>
          <button type='submit' className='submit_btn'>
            Submit
          </button>
        </form>
      </div>
    </div>
  )
})

export default Form
