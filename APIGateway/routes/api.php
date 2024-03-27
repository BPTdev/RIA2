<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Storage;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Log;


/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
|
*/

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});

Route::post('/analyze', function (Request $request) {
    if ($request->hasFile('image') && $request->file('image')->isValid()) {
        $response = Http::attach(
            'file',
            file_get_contents($request->file('image')->path()),
            $request->file('image')->getClientOriginalName()
        )
        ->asMultipart()
        ->post('http://localhost:5171/analyze', [
            ['name' => 'max_labels', 'contents' => $request->input('max_labels')],
            ['name' => 'min_confidence', 'contents' => $request->input('min_confidence')]
        ]);
        return response()->json($response->json());
    } else {
        return response()->json(['error' => 'No valid image provided'], 400);
    }
});