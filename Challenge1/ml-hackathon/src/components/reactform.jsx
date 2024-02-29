import { useForm } from "react-hook-form";
import { DevTool } from "@hookform/devtools";
import { useState, useEffect } from "react";

export default function Form() {
	const [data,setData]=useState([]);

	const form = useForm();
	const { register, control, handleSubmit, watch, reset, formState: { errors, touched } } = form;

	const onSubmit = (formData) => {
		setData([...data, formData]);
		// console.log(formData["age"]);
		const filteredData = new FormData();
		const jsonData = JSON.stringify(formData);

		// console.log(jsonData);
		// console.log(filteredData);
		// console.log(filteredData.append("key", "value"))
		// console.log(jsonData.key;)

		filteredData.append("workshopName", formData['workshopName']);
		console.log(filteredData.get('workshopName'));
		filteredData.append("proNouns", formData['proNouns']);
		filteredData.append("age", formData['age']);
		
		filteredData.append("ethnicity", formData['ethnicity']);
		filteredData.append("disability", formData['disability']);
		filteredData.append("employmentStatus", formData['employmentStatus']);
		filteredData.append("location", formData['location']);
		filteredData.append("nHousehold", formData['nHousehold']);
		filteredData.append("income", formData['income']);
	}

	// useEffect(() => {
	// 	if (data.length > 0) {
	// 	  const filteredData = data.map(({ age, disability, employmentStatus }) => ({ age, disability, employmentStatus }));
	// 	  const jsonData = JSON.stringify(filteredData);
		  
	// 	  const formData = new FormData();
	// 	  formData.append("age", filteredData['age']);
		  
	// 	  // Now you can use the formData for your intended purpose
	// 	  console.log(filteredData); 
	// 	  console.log(jsonData);
	// 	  console.log(formData.get("age"));
	// 	}
	//   }, [data]);


	return (
		<>
			<form onSubmit={handleSubmit(onSubmit)}>
				<label htmlFor="workshopName">What is the workshoop name?</label>
				<input id="workshopName" type="text" {...register("workshopName", {
					required:{
						value: true,
						message: "Workshop name is required"
					},
				})} />
				<p className="error">{errors.workshopName?.message}</p>
				<label htmlFor="gender">What is your gender?</label>
				<select id="gender" type="select" {...register("gender", {
					required:{
						value: true,
						message: "Please selection an option"
					},
				})}>
				<option value="none"> Select an option</option>
				<option value="male">Male</option>
				<option value="female">Female</option>
				<option value="non-binary">Non-binary</option>
				<option value="other">Other</option>
				</select>
				<p className="error">{errors.gender?.message}</p>

				<label htmlFor="proNouns">What are your prounouns?</label>
				<select id="proNouns" type="select" {...register("proNouns", {
					required:{
						value: true,
						message: "Please selection an option"
					},
				})}>
					<option value="none"> Select an option</option>
				<option value="they/them">They/them</option>
				<option value="she/her">She/her</option>
				<option value="he/him">He/him</option>
				<option value="other">Other</option>
				</select>
				<p className="error">{errors.proNouns?.message}</p>

				<label htmlFor="age">What is your age?</label>
				<select id="age" type="select" {...register("age", {
					required:{
						value: true,
						message: "Please selection an option"
					},
				})}>
				<option value="none"> Select an option</option>
				<option value="18-24">18-24</option>
				<option value="25-34">25-34</option>
				<option value="35-44">35-44</option>
				<option value="45-54">45-54</option>
				<option value="55-64">55-64</option>
				<option value="65+">65+</option>
				</select>
				<p className="error">{errors.age?.message}</p>

				<label htmlFor="ethnicity">What is your ethnicity?</label>
				<select id="ethnicity" type="text" {...register("ethnicity", {
					required:{
						value: true,
						message: "Please selection an option"
					},
				})}>
				<option value="none"> Select an option</option>
				<option value="white">White</option>
				<option value="black">Black</option>
				<option value="asian">Asian</option>
				<option value="asian">Asian</option>
				<option value="other">Other</option>
				</select>
				<p className="error">{errors.ethnicity?.message}</p>

				<label htmlFor="disability">Do you have a disability?</label>
				<select id="disability" type="text" {...register("disability", {
					required:{
						value: true,
						message: "Please selection an option"
					},
				})}>
					<option value="none"> Select an option</option>
				<option value="yes">Yes</option>
				<option value="no">No</option>
				</select>
				<input type="text" placeholder="If yes, please specify" />
				<p className="error">{errors.disability?.message}</p>

				<label htmlFor="employStatus">What is your employment status?</label>
				<select id="employ-status" type="text" {...register("employ-status", {
					required:{
						value: true,
						message: "Please selection an option"
					},
				})}>
				<option value="none"> Select an option</option>
				<option value="full-time">Full-time</option>
				<option value="part-time">Part-time</option>
				<option value="self-employed">Self-employed</option>
				<option value="unemployed">Unemployed</option>
				<option value="student">Student</option>
				<option value="retired">Retired</option>
				</select>
				<p className="error">{errors.employStatus?.message}</p>

				<label htmlFor="location">From the following locations, where are you situated?</label>
				<select id="location" type="text" {...register("location", {
					required:{
						value: true,
						message: "Please selection an option"
					},
				})}>
				<option value="none"> Select an option</option>
				<option value="north-east">North East</option> 
				<option value="north-west">North West</option> 
				<option value="yorkshire">Yorkshire adn the Humber</option>
				<option value="east-midlands">East Midlands</option>
				<option value="west-midlands">West Midlands</option>
				<option value="east">East of England</option>
				<option value="london">London</option>
				<option value="south-east">South East</option> 
				<option value="south-west">South West</option>
				</select>
				<p className="error">{errors.location?.message}</p>

				<label htmlFor="nHousehold">How many people live in your household?</label>
				<select id="nHousehold" type="text" {...register("nHousehold", {
					required:{
						value: true,
						message: "Please selection an option"
					},
				})}>
				<option value="none"> Select an option</option>
				<option value="0">0</option>	
				<option value="1">1</option>
				<option value="2">2</option>
				<option value="3">3</option>
				<option value="4">4</option>
				<option value="5+">5+</option>
				</select>
				<p className="error">{errors.nHousehold?.message}</p>

				<label htmlFor="nHousehold">Is anyone in your household:</label>
				<select id="nHousehold" type="text" {...register("nHousehold", {
					required:{
						value: true,
						message: "Please selection an option"
					},
				})}>
				<option value="none">Select an option</option>
				<option value="0">Below 16 years old</option>	
				<option value="1">Disabled</option>
				<option value="2">Retired</option>
				<option value="3">Long-term health condition</option>
				<option value="4">Other</option>
				<option value="5+">None of the above</option>
				</select>
				<input type="text" placeholder="If other, please specify" />
				<p className="error">{errors.nHousehold?.message}</p>

				<label htmlFor="income">Which income bracket are you part of?</label>
				<select id="income" type="text" {...register("income", {
					required:{
						value: true,
						message: "Please selection an option"
					},
				})}>
					<option value="none"> Select an option</option>
					<option value="<10,000">Less than £10,000</option> <option value="10,000-19,999">£10,000 - £19,999</option>
					<option value="20,000-29,999">£20,000 - £29,999</option>
					<option value="30,000-39,999">£30,000 - £39,999</option>
					<option value="40,000-49,999">£40,000 - £49,999</option>
					<option value="50,000-59,999">£50,000 - £59,999</option>
					<option value="60,000-69,999">£60,000 - £69,999</option>
					<option value="70,000-79,999">£70,000 - £79,999</option>
					<option value="80,000-89,999">£80,000 - £89,999+</option>
				</select>
				<p className="error">{errors.income?.message}</p>

				
				<button type="submit" onClick={() => handleSubmit(onSubmit)}>Submit</button>
			</form>
			<DevTool control={control} />
		</>
	);
}
