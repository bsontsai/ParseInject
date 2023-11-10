package com.example;

import org.junit.Test;

public class TestSampleInput {
	@Test
	public void testSampleInput1() {
		SampleInput1 si = new SampleInput1();
		si.test(10);
	}

	@Test
	public void testSampleInput2() {
		SampleInput2 si = new SampleInput2();
		si.test(20);
	}

	@Test
	public void testSampleInput3() {
		SampleInput3 si = new SampleInput3();
		si.test(30);
	}

}