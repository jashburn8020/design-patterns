package com.jashburn.designpatterns.behavioural.command;

import static org.mockito.ArgumentMatchers.anyLong;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.never;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.mockito.junit.MockitoJUnit;
import org.mockito.junit.MockitoRule;
import org.mockito.quality.Strictness;

public class StoreWidgetMetadataCommandTest {

	@Rule
	public MockitoRule rule = MockitoJUnit.rule().strictness(Strictness.STRICT_STUBS);

	private Receiver mockReceiver;
	private String metadata;
	private long metadataId;

	@Before
	public void setUp() throws Exception {
		mockReceiver = mock(Receiver.class);
		metadata = "test string";
		metadataId = 111l;
	}

	@Test
	public void testExecuteUndo() {
		when(mockReceiver.storeMetadata(metadata)).thenReturn(metadataId);

		StoreWidgetMetadataCommand command = new StoreWidgetMetadataCommand(mockReceiver, metadata);
		command.execute();
		verify(mockReceiver).storeMetadata(metadata);

		command.undo();
		verify(mockReceiver).deleteMetadata(metadataId);
	}

	@Test
	public void testExecuteTwice() {
		when(mockReceiver.storeMetadata(metadata)).thenReturn(metadataId);

		StoreWidgetMetadataCommand command = new StoreWidgetMetadataCommand(mockReceiver, metadata);
		command.execute();
		command.execute();
		verify(mockReceiver, times(1)).storeMetadata(metadata);
	}
	
	@Test
	public void testUndoNoExecute() {
		StoreWidgetMetadataCommand command = new StoreWidgetMetadataCommand(mockReceiver, metadata);
		command.undo();
		command.undo();
		verify(mockReceiver, never()).deleteMetadata(anyLong());
		
	}
}
